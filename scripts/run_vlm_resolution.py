#!/usr/bin/env python3
import csv
import json
import os
import re
import shutil
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

SERVER = "http://127.0.0.1:8081"
MODEL = "Qwen2.5-VL-72B-Instruct-Q4_K_M.gguf"
IMAGE_DIR = Path("resolution_samples")
SERVER_LOG_FILE = Path("logs/vlm_server.log")
QUESTION = "What is happening in this image? Describe the animals, their approximate number, activity, environment, and colors. Which animal appears to be the leader of the group, and what five visual clues made you reach that conclusion? Use no more than 50 words."
MAX_TOKENS = 16
TIMEOUT_S = 900
GPU_SAMPLE_INTERVAL_S = 0.5

RUN_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_DIR = Path("reports") / RUN_ID
REPORT_FILE = REPORT_DIR / "vlm_resolution_report.csv"
RUN_LOG_FILE = REPORT_DIR / "vlm_run.log"
SERVER_LOG_COPY = REPORT_DIR / "vlm_server.log"
GPU_LOG_FILE = REPORT_DIR / "gpu_usage.csv"

IMAGE_EXTS = {".jpg", ".jpeg", ".JPG", ".JPEG", ".png", ".PNG"}
SKIP_NAME_PARTS = ("24MP", "6000x4000")

CONFIG_ENV_KEYS = [
    "TURBOPREFILL",
    "CTX_SIZE",
    "BATCH_SIZE",
    "UBATCH_SIZE",
    "N_GPU_LAYERS",
    "SPLIT_MODE",
    "TENSOR_SPLIT",
    "FLASH_ATTN",
    "CACHE_TYPE_K",
    "CACHE_TYPE_V",
    "IMAGE_MIN_TOKENS",
    "IMAGE_MAX_TOKENS",
    "HOST",
    "PORT",
    "CACHE_RAM",
    "PROMPT_CACHE",
    "METRICS",
    "WEBUI",
    "WARMUP",
    "OFFLINE",
    "MEDIA_PATH",
]


def sh(cmd: list[str]) -> str:
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
    except Exception as e:
        return f"ERROR running {' '.join(cmd)}: {e}\n"


def env_value(name: str) -> str:
    return os.environ.get(name, "")


def request_image(filename: str) -> dict:
    payload = {
        "model": MODEL,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": QUESTION},
                {"type": "image_url", "image_url": {"url": f"file://./{filename}"}},
            ],
        }],
        "max_tokens": MAX_TOKENS,
    }

    data = json.dumps(payload).encode("utf-8")
    req = Request(
        f"{SERVER}/v1/chat/completions",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urlopen(req, timeout=TIMEOUT_S) as r:
        return json.loads(r.read().decode("utf-8"))


def get_resolution_tuple(path: Path) -> tuple[int, int]:
    try:
        out = subprocess.check_output(["file", str(path)], text=True)
    except Exception:
        return (0, 0)

    m = re.search(r"(\d+)x(\d+)", out)
    if not m:
        return (0, 0)
    return int(m.group(1)), int(m.group(2))


def get_resolution(path: Path) -> str:
    w, h = get_resolution_tuple(path)
    return f"{w}x{h}" if w and h else ""


def pixel_count(path: Path) -> int:
    w, h = get_resolution_tuple(path)
    return w * h


def parse_last_log_block() -> dict:
    if not SERVER_LOG_FILE.exists():
        return {}

    text = SERVER_LOG_FILE.read_text(errors="ignore")
    blocks = text.split("srv  handle_media: loading image from local file")
    block = blocks[-1] if len(blocks) > 1 else text[-5000:]

    def find(pattern, default=""):
        m = re.search(pattern, block)
        return m.group(1) if m else default

    return {
        "visual_tokens": find(r"n_tokens_batch\s*=\s*(\d+)"),
        "image_slice_encoded_ms": find(r"image slice encoded in\s+(\d+)\s+ms"),
        "image_decoded_ms": find(r"image decoded .* in\s+(\d+)\s+ms"),
        "image_processed_ms": find(r"image processed in\s+(\d+)\s+ms"),
        "prompt_eval_ms": find(r"prompt eval time =\s*([\d.]+)\s+ms"),
        "prompt_tokens": find(r"prompt eval time =\s*[\d.]+\s+ms\s*/\s*(\d+)\s+tokens"),
        "prompt_tok_s": find(r"prompt eval time =.*?,\s*([\d.]+)\s+tokens per second\)"),
        "generation_ms": find(r"\n\s*eval time =\s*([\d.]+)\s+ms"),
        "generation_tokens": find(r"\n\s*eval time =\s*[\d.]+\s+ms\s*/\s*(\d+)\s+tokens"),
        "generation_tok_s": find(r"\n\s*eval time =.*?,\s*([\d.]+)\s+tokens per second\)"),
        "total_ms": find(r"total time =\s*([\d.]+)\s+ms"),
        "total_tokens": find(r"total time =\s*[\d.]+\s+ms\s*/\s*(\d+)\s+tokens"),
        "turboprefill_requested": find(r"TurboPrefill requested=(\d+)"),
        "turboprefill_active": find(r"active=(\d+)"),
        "n_ubatch": find(r"n_ubatch=(\d+)"),
        "full_ubatches": find(r"full_ubatches=(\d+)"),
        "tpdbg_has_tokens": find(r"has_tokens=(\d+)"),
        "tpdbg_has_embd": find(r"has_embd=(\d+)"),
        "tpdbg_positions_contiguous": find(r"positions_contiguous=(\d+)"),
        "tpdbg_single_seq": find(r"single_seq=(\d+)"),
    }


def get_latest_server_settings() -> dict:
    if not SERVER_LOG_FILE.exists():
        return {}
    text = SERVER_LOG_FILE.read_text(errors="ignore")

    def last(pattern, default=""):
        matches = re.findall(pattern, text)
        return matches[-1] if matches else default

    return {
        "server_n_ctx": last(r"llama_context: n_ctx\s*=\s*(\d+)"),
        "server_n_batch": last(r"llama_context: n_batch\s*=\s*(\d+)"),
        "server_n_ubatch": last(r"llama_context: n_ubatch\s*=\s*(\d+)"),
        "server_causal_attn": last(r"llama_context: causal_attn\s*=\s*(\d+)"),
        "server_flash_attn": last(r"llama_context: flash_attn\s*=\s*([^\n]+)"),
        "server_pipeline_parallel": "1" if "pipeline parallelism enabled" in text else "",
        "server_graph_splits": last(r"sched_reserve: graph splits = (\d+)"),
        "server_sched_copies": last(r"sched_reserve: reserve took .* sched copies = (\d+)"),
        "server_clip_backend": last(r"clip_ctx: CLIP using ([^\n]+) backend"),
        "server_image_min_pixels": last(r"image_min_pixels:\s*(\d+)"),
        "server_image_max_pixels": last(r"image_max_pixels:\s*(\d+)"),
    }


def get_model_buffers_summary() -> str:
    if not SERVER_LOG_FILE.exists():
        return ""
    lines = []
    for line in SERVER_LOG_FILE.read_text(errors="ignore").splitlines():
        if "model buffer size" in line or "KV buffer size" in line or "compute buffer size" in line:
            lines.append(line)
    return " | ".join(lines[-80:])


def write_run_log(files: list[Path]) -> None:
    settings = get_latest_server_settings()
    with RUN_LOG_FILE.open("w", encoding="utf-8") as f:
        f.write(f"RUN_ID={RUN_ID}\n")
        f.write(f"START_TIME={datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"SERVER={SERVER}\n")
        f.write(f"MODEL={MODEL}\n")
        f.write(f"IMAGE_DIR={IMAGE_DIR}\n")
        f.write(f"QUESTION={QUESTION}\n")
        f.write(f"MAX_TOKENS={MAX_TOKENS}\n")
        f.write(f"TIMEOUT_S={TIMEOUT_S}\n")
        f.write(f"GPU_SAMPLE_INTERVAL_S={GPU_SAMPLE_INTERVAL_S}\n\n")

        f.write("ENV SETTINGS:\n")
        for key in CONFIG_ENV_KEYS:
            f.write(f"{key}={env_value(key)}\n")

        f.write("\nPARSED SERVER SETTINGS:\n")
        for key, value in settings.items():
            f.write(f"{key}={value}\n")

        f.write("\nMODEL/KV/COMPUTE BUFFERS SUMMARY:\n")
        f.write(get_model_buffers_summary() + "\n")

        f.write("\nNVIDIA-SMI START:\n")
        f.write(sh(["nvidia-smi"]))

        f.write("\nFILES ORDER:\n")
        for p in files:
            f.write(f"{get_resolution(p)} {p.name} {p.stat().st_size}\n")


def append_run_log(text: str) -> None:
    with RUN_LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(text)
        if not text.endswith("\n"):
            f.write("\n")


def init_gpu_log() -> None:
    with GPU_LOG_FILE.open("w", encoding="utf-8") as f:
        f.write("tag,unix_time,timestamp,index,gpu_util_pct,mem_used_mib,mem_free_mib,power_w,temp_c\n")


def sample_gpu_once(tag: str) -> None:
    out = sh([
        "nvidia-smi",
        "--query-gpu=timestamp,index,utilization.gpu,memory.used,memory.free,power.draw,temperature.gpu",
        "--format=csv,noheader,nounits",
    ])
    now = f"{time.time():.3f}"
    with GPU_LOG_FILE.open("a", encoding="utf-8") as f:
        for line in out.strip().splitlines():
            if line.startswith("ERROR"):
                f.write(f"{tag},{now},ERROR,,,,,,{line}\n")
            else:
                f.write(f"{tag},{now},{line}\n")


class GpuSampler:
    def __init__(self, tag: str):
        self.tag = tag
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        while not self.stop_event.is_set():
            sample_gpu_once(self.tag)
            self.stop_event.wait(GPU_SAMPLE_INTERVAL_S)

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.stop_event.set()
        self.thread.join(timeout=2.0)
        sample_gpu_once(self.tag + "_end")


def summarize_gpu_for_tag(tag_prefix: str) -> dict:
    if not GPU_LOG_FILE.exists():
        return {}
    max_util = 0
    max_mem = 0
    max_power = 0.0
    samples = 0
    try:
        with GPU_LOG_FILE.open("r", encoding="utf-8") as f:
            next(f, None)
            for line in f:
                parts = [p.strip() for p in line.rstrip("\n").split(",")]
                if len(parts) < 9 or not parts[0].startswith(tag_prefix):
                    continue
                try:
                    util = int(float(parts[4]))
                    mem = int(float(parts[5]))
                    power = float(parts[7]) if parts[7] else 0.0
                except Exception:
                    continue
                max_util = max(max_util, util)
                max_mem = max(max_mem, mem)
                max_power = max(max_power, power)
                samples += 1
    except Exception:
        pass
    return {
        "gpu_samples": samples,
        "gpu_max_util_pct": max_util if samples else "",
        "gpu_max_mem_used_mib": max_mem if samples else "",
        "gpu_max_power_w": f"{max_power:.1f}" if samples else "",
    }


def make_empty_row(path: Path) -> dict:
    settings = get_latest_server_settings()
    row = {
        "run_id": RUN_ID,
        "file": path.name,
        "resolution": get_resolution(path),
        "pixel_count": pixel_count(path),
        "size_bytes": path.stat().st_size,
        "model": MODEL,
        "server": SERVER,
        "question": QUESTION,
        "max_tokens": MAX_TOKENS,
        "env_turboprefill": env_value("TURBOPREFILL"),
        "env_ctx_size": env_value("CTX_SIZE"),
        "env_batch_size": env_value("BATCH_SIZE"),
        "env_ubatch_size": env_value("UBATCH_SIZE"),
        "env_tensor_split": env_value("TENSOR_SPLIT"),
        "env_n_gpu_layers": env_value("N_GPU_LAYERS"),
        "env_split_mode": env_value("SPLIT_MODE"),
        "env_flash_attn": env_value("FLASH_ATTN"),
        "env_cache_type_k": env_value("CACHE_TYPE_K"),
        "env_cache_type_v": env_value("CACHE_TYPE_V"),
        "env_image_min_tokens": env_value("IMAGE_MIN_TOKENS"),
        "env_image_max_tokens": env_value("IMAGE_MAX_TOKENS"),
        **settings,
        "visual_tokens": "",
        "image_slice_encoded_ms": "",
        "image_decoded_ms": "",
        "image_processed_ms": "",
        "prompt_eval_ms": "",
        "prompt_tokens": "",
        "prompt_tok_s": "",
        "generation_ms": "",
        "generation_tokens": "",
        "generation_tok_s": "",
        "total_ms": "",
        "total_tokens": "",
        "turboprefill_requested": "",
        "turboprefill_active": "",
        "n_ubatch": "",
        "full_ubatches": "",
        "tpdbg_has_tokens": "",
        "tpdbg_has_embd": "",
        "tpdbg_positions_contiguous": "",
        "tpdbg_single_seq": "",
        "gpu_samples": "",
        "gpu_max_util_pct": "",
        "gpu_max_mem_used_mib": "",
        "gpu_max_power_w": "",
        "status": "",
        "error": "",
        "answer": "",
    }
    return row


def copy_server_log() -> None:
    if SERVER_LOG_FILE.exists():
        shutil.copy2(SERVER_LOG_FILE, SERVER_LOG_COPY)


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    init_gpu_log()

    files = [p for p in IMAGE_DIR.iterdir() if p.is_file() and p.suffix in IMAGE_EXTS]
    files = [p for p in files if not any(s in p.name for s in SKIP_NAME_PARTS)]
    files = sorted(files, key=lambda p: (pixel_count(p), p.name.lower()))

    write_run_log(files)

    base_row = make_empty_row(files[0]) if files else {}
    fields = list(base_row.keys())

    print("ORDER:")
    for p in files:
        print(f"  {get_resolution(p):>10}  {p.name}")

    with REPORT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for path in files:
            row = make_empty_row(path)
            tag = re.sub(r"[^A-Za-z0-9_.-]+", "_", path.name)
            print(f"RUN: {row['resolution']} {path.name}", flush=True)
            append_run_log(f"\nRUN {datetime.now().isoformat(timespec='seconds')} {row['resolution']} {path.name}")

            try:
                sample_gpu_once(f"before_{tag}")
                t0 = time.time()
                with GpuSampler(f"during_{tag}"):
                    resp = request_image(path.name)
                api_wall_ms = (time.time() - t0) * 1000.0
                sample_gpu_once(f"after_{tag}")
                time.sleep(0.5)

                log = parse_last_log_block()
                answer = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
                gpu_summary = summarize_gpu_for_tag(f"during_{tag}")

                row.update(log)
                row.update(gpu_summary)
                row["status"] = "ok"
                row["answer"] = answer.replace("\n", " ")
                append_run_log(
                    f"OK {path.name}: wall_ms={api_wall_ms:.2f} "
                    f"visual={row.get('visual_tokens','')} "
                    f"img_dec_ms={row.get('image_decoded_ms','')} "
                    f"prompt_tok_s={row.get('prompt_tok_s','')} "
                    f"tp_active={row.get('turboprefill_active','')} "
                    f"gpu_max_util={row.get('gpu_max_util_pct','')}"
                )

            except HTTPError as e:
                row["status"] = "http_error"
                row["error"] = f"HTTPError {e.code}: {e.reason}"
                row.update(parse_last_log_block())
                row.update(summarize_gpu_for_tag(f"during_{tag}"))
                writer.writerow(row)
                f.flush()
                append_run_log(f"FAIL {path.name}: {row['error']}")
                print(f"FAIL: {path.name}: {row['error']}", flush=True)
                break

            except URLError as e:
                row["status"] = "server_down_or_no_reply"
                row["error"] = str(e.reason)
                row.update(parse_last_log_block())
                row.update(summarize_gpu_for_tag(f"during_{tag}"))
                writer.writerow(row)
                f.flush()
                append_run_log(f"FAIL {path.name}: {row['error']}")
                print(f"FAIL: {path.name}: {row['error']}", flush=True)
                break

            except Exception as e:
                row["status"] = "error"
                row["error"] = repr(e)
                row.update(parse_last_log_block())
                row.update(summarize_gpu_for_tag(f"during_{tag}"))
                writer.writerow(row)
                f.flush()
                append_run_log(f"FAIL {path.name}: {row['error']}")
                print(f"FAIL: {path.name}: {row['error']}", flush=True)
                break

            writer.writerow(row)
            f.flush()

            print(
                f"  ok visual={row['visual_tokens']} "
                f"img_enc={row['image_slice_encoded_ms']}ms "
                f"img_dec={row['image_decoded_ms']}ms "
                f"prompt={row['prompt_tok_s']} tok/s "
                f"gen={row['generation_tok_s']} tok/s "
                f"tp={row['turboprefill_active']} "
                f"gpu_max={row['gpu_max_util_pct']}%",
                flush=True,
            )

    append_run_log(f"\nEND_TIME={datetime.now().isoformat(timespec='seconds')}")
    append_run_log("\nNVIDIA-SMI END:\n" + sh(["nvidia-smi"]))
    copy_server_log()

    print(f"REPORT_DIR: {REPORT_DIR}")
    print(f"CSV: {REPORT_FILE}")
    print(f"RUN_LOG: {RUN_LOG_FILE}")
    print(f"SERVER_LOG: {SERVER_LOG_COPY}")
    print(f"GPU_LOG: {GPU_LOG_FILE}")


if __name__ == "__main__":
    main()
