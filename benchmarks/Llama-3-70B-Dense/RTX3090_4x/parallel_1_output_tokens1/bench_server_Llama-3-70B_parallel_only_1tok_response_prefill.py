import csv
import os
import re
import signal
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

import requests

CONFIG_PATH = "server_config_Llama-3-70B.sh"
SCRIPT_DIR = Path(__file__).resolve().parent

SERVER_READY_TIMEOUT_S = 920
REQUEST_TIMEOUT_S = 3600

# Parallel-only 1-token response benchmark:
#   For every ctx_*.txt file, the script runs exactly PARALLEL concurrent requests.
#   It does not run active_slots=1..PARALLEL.
#   Each request is forced to n_predict=1, regardless of N_GEN in the config.
#   Decode metrics are not written to CSV/report.
#   Per-request prefill timings are the values returned by llama-server.
#   Group metrics marked with * are computed by this script:
#       total prompt tokens across all requests / wall time from releasing the group
#       to receiving the last HTTP response.


def load_cfg(path=CONFIG_PATH):
    cfg = {}
    text = Path(path).read_text(encoding="utf-8")

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)

        v = value.strip().strip('"').strip("'")
        v = v.replace("$SCRIPT_DIR", str(SCRIPT_DIR))
        cfg[key.strip()] = os.path.expandvars(v)

    defaults = {
        "MODEL": "$HOME/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf",
        "CONTEXTS_DIR": "$HOME/workspace/projects/llama.cpp/contexts_llama3_70b",
        "OUTPUT_DIR": "$HOME/workspace/projects/llama.cpp/bench_reports_Llama3_70B",
        "HOST": "127.0.0.1",
        "PORT": "8081",
        "NGL": "99",
        "CTX_SIZE": "131072",
        "N_GEN": "128",
        "BATCH": "4096",
        "UBATCH": "32",
        "PARALLEL": "1",
        "CTK": "f16",
        "SPLIT_MODE": "layer",
        "TENSOR_SPLIT": "5/7/7/7/7/7/7/7/7/7/7/6",
        "TEMPERATURE": "0.0",
        "MONITOR_INTERVAL": "1",
        "GGML_SCHED_DEBUG": "0",
        "GGML_CUDA_DEBUG": "0",
    }

    for key, value in defaults.items():
        cfg.setdefault(key, os.path.expandvars(value))

    return cfg


cfg = load_cfg()


def nvidia_sample():
    out = subprocess.check_output([
        "nvidia-smi",
        "--query-gpu=index,name,pci.bus_id,pcie.link.gen.current,pcie.link.width.current,utilization.gpu,power.draw,memory.used",
        "--format=csv,noheader,nounits",
    ], text=True)

    rows = []
    for line in out.strip().splitlines():
        parts = [x.strip() for x in line.split(",")]
        rows.append({
            "gpu": int(parts[0]),
            "name": parts[1],
            "bus": parts[2],
            "gen": parts[3],
            "width": parts[4],
            "util": float(parts[5]),
            "power": float(parts[6]),
            "mem": float(parts[7]),
            "t": time.time(),
        })
    return rows


class Monitor:
    def __init__(self, interval):
        self.interval = float(interval)
        self.samples = []
        self.stop_flag = False
        self.thread = threading.Thread(target=self.run, daemon=True)

    def start(self):
        self.thread.start()

    def stop(self):
        self.stop_flag = True
        self.thread.join(timeout=2)

    def run(self):
        while not self.stop_flag:
            try:
                self.samples.extend(nvidia_sample())
            except Exception:
                pass
            time.sleep(self.interval)


def avg_gpu(samples, t0, t1):
    selected = [s for s in samples if t0 <= s["t"] <= t1]
    out = {}

    for gpu in sorted(set(s["gpu"] for s in selected)):
        gpu_samples = [s for s in selected if s["gpu"] == gpu]
        if not gpu_samples:
            continue

        out[gpu] = {
            "name": gpu_samples[-1]["name"],
            "pcie": f"Gen{gpu_samples[-1]['gen']} x{gpu_samples[-1]['width']}",
            "util_avg": sum(x["util"] for x in gpu_samples) / len(gpu_samples),
            "util_max": max(x["util"] for x in gpu_samples),
            "power_avg": sum(x["power"] for x in gpu_samples) / len(gpu_samples),
            "power_max": max(x["power"] for x in gpu_samples),
            "mem_max": max(x["mem"] for x in gpu_samples),
            "samples": len(gpu_samples),
        }

    return out


def fmt(value, nd=2):
    if value is None:
        return "n/a"
    try:
        return f"{float(value):.{nd}f}"
    except Exception:
        return str(value)


def start_server(out_dir):
    subprocess.run("pkill -f llama-server || true", shell=True)

    log_path = out_dir / "llama_server.log"
    log = open(log_path, "w", encoding="utf-8")

    cmd = [
        "./build/bin/llama-server",
        "-m", cfg["MODEL"],
        "--host", cfg["HOST"],
        "--port", str(cfg["PORT"]),
        "-ngl", str(cfg["NGL"]),
        "-c", str(cfg["CTX_SIZE"]),
        "--override-kv", f"llama.context_length=int:{cfg['CTX_SIZE']}",
        "-b", str(cfg["BATCH"]),
        "-ub", str(cfg["UBATCH"]),
        "-np", str(cfg["PARALLEL"]),
        "-ctk", cfg["CTK"],
        "-sm", cfg["SPLIT_MODE"],
        "-ts", cfg["TENSOR_SPLIT"],
    ]

    env = os.environ.copy()
    env["GGML_SCHED_DEBUG"] = cfg.get("GGML_SCHED_DEBUG", "0")

    if cfg.get("GGML_CUDA_DEBUG", "0") != "0":
        env["GGML_CUDA_DEBUG"] = cfg["GGML_CUDA_DEBUG"]

    proc = subprocess.Popen(
        cmd,
        stdout=log,
        stderr=subprocess.STDOUT,
        text=True,
        env=env,
    )

    url = f"http://{cfg['HOST']}:{cfg['PORT']}/v1/models"
    for _ in range(SERVER_READY_TIMEOUT_S):
        if proc.poll() is not None:
            log.close()
            tail = log_path.read_text(encoding="utf-8", errors="ignore").splitlines()[-80:]
            raise RuntimeError("llama-server exited during startup. Last log lines:\n" + "\n".join(tail))

        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return proc, log_path, cmd
        except Exception:
            pass

        time.sleep(1)

    proc.terminate()
    log.close()
    raise RuntimeError(f"llama-server did not start within {SERVER_READY_TIMEOUT_S} seconds. Log: {log_path}")


def make_payload(prompt):
    return {
        "prompt": prompt,
        "n_predict": 1,
        "temperature": float(cfg["TEMPERATURE"]),
        "top_k": 1,
        "top_p": 1.0,
        "min_p": 0.0,
        "cache_prompt": False,
        "stream": False,
    }


def request_many_prepared(url, payload, count):
    results = [None] * count
    errors = [None] * count
    start_event = threading.Event()

    def worker(i):
        try:
            start_event.wait()
            t0 = time.time()
            response = requests.post(url, json=payload, timeout=REQUEST_TIMEOUT_S)
            t1 = time.time()
            response.raise_for_status()
            results[i] = (t0, t1, response.json())
        except Exception as exc:
            errors[i] = exc

    threads = []
    for i in range(count):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        t.start()
        threads.append(t)

    # The timestamp is intentionally taken immediately before releasing all workers.
    group_start = time.time()
    start_event.set()

    for t in threads:
        t.join()

    group_end = time.time()

    failed = [(i + 1, err) for i, err in enumerate(errors) if err is not None]
    if failed:
        msg = "; ".join(f"request {i}: {err}" for i, err in failed)
        raise RuntimeError(f"One or more concurrent requests failed: {msg}")

    return group_start, group_end, results


def prompt_size_from_name(path):
    match = re.search(r"ctx_(?:\d+_)?(\d+)", path.name)
    return int(match.group(1)) if match else 0


def collect_environment():
    info = {
        "TURBOPREFILL": os.environ.get("TURBOPREFILL", "0"),
    }

    commands = {
        "nvidia_smi": ["nvidia-smi", "--query-gpu=index,name,driver_version,memory.total", "--format=csv,noheader"],
        "nvcc": ["nvcc", "--version"],
        "cmake": ["cmake", "--version"],
    }

    for key, cmd in commands.items():
        try:
            info[key] = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT).strip()
        except Exception as exc:
            info[key] = f"unavailable: {exc}"

    return info


def row_from_response(ctx, active_slots, request_index, t0, t1, data, monitor_samples):
    timings = data.get("timings", {})
    usage = data.get("usage", {})

    prompt_ms = float(timings.get("prompt_ms", 0))
    prefill_tps = float(timings.get("prompt_per_second", 0))

    prompt_tokens = usage.get("prompt_tokens") or data.get("tokens_evaluated")

    pre_t0 = t0
    pre_t1 = t0 + prompt_ms / 1000.0

    return {
        "file": ctx.name,
        "active_slots": active_slots,
        "request_index": request_index,
        "prompt_target": prompt_size_from_name(ctx),
        "prompt_tokens": prompt_tokens,
        "prefill_ms": prompt_ms,
        "prefill_tps": prefill_tps,
        "wall_ms": (t1 - t0) * 1000.0,
        "pre": avg_gpu(monitor_samples, pre_t0, pre_t1),
    }


def group_row_from_results(ctx, active_slots, group_start, group_end, request_rows, monitor_samples):
    group_wall_ms = (group_end - group_start) * 1000.0
    group_prompt_tokens = sum(int(row["prompt_tokens"] or 0) for row in request_rows)
    group_response_tok_s = None
    if group_wall_ms > 0:
        group_response_tok_s = group_prompt_tokens / (group_wall_ms / 1000.0)

    return {
        "file": ctx.name,
        "active_slots": active_slots,
        "group_start_epoch": group_start,
        "group_end_epoch": group_end,
        "group_wall_ms": group_wall_ms,
        "group_prompt_tokens": group_prompt_tokens,
        "group_response_tok_s": group_response_tok_s,
        "gpu": avg_gpu(monitor_samples, group_start, group_end),
    }


def write_report(report, raw_csv, group_csv, results, group_results, server_log, server_cmd, env_info):
    with open(raw_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "file",
            "active_slots",
            "request_index",
            "prompt_tokens",
            "prefill_ms",
            "prefill_tok_s",
            "wall_ms",
        ])
        for row in results:
            writer.writerow([
                row["file"],
                row["active_slots"],
                row["request_index"],
                row["prompt_tokens"],
                row["prefill_ms"],
                row["prefill_tps"],
                row["wall_ms"],
            ])

    with open(group_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "file",
            "active_slots",
            "group_start_epoch",
            "group_end_epoch",
            "group_wall_ms*",
            "group_prompt_tokens*",
            "group_response_tok_s*",
        ])
        for row in group_results:
            writer.writerow([
                row["file"],
                row["active_slots"],
                row["group_start_epoch"],
                row["group_end_epoch"],
                row["group_wall_ms"],
                row["group_prompt_tokens"],
                row["group_response_tok_s"],
            ])

    with open(report, "w", encoding="utf-8") as f:
        f.write("# llama-server PARALLEL-only 1-token response benchmark report\n\n")

        f.write("## Test header\n\n")
        for key in ["MODEL", "NGL", "CTX_SIZE", "N_GEN", "BATCH", "UBATCH", "CTK", "SPLIT_MODE", "TENSOR_SPLIT", "PARALLEL", "TEMPERATURE"]:
            f.write(f"- {key}: `{cfg[key]}`\n")
        f.write("- Effective n_predict: `1` forced by benchmark script\n")
        f.write(f"- TURBOPREFILL: `{env_info['TURBOPREFILL']}`\n")
        f.write("- Parallel mode: `active_slots = PARALLEL only`\n")
        f.write("- Decode metrics: `not written`\n")
        f.write("- Group metrics marked `*`: `computed by benchmark script`\n")
        f.write(f"- llama_server_log: `{server_log}`\n\n")

        f.write("## Environment\n\n")
        for key, value in env_info.items():
            f.write(f"### {key}\n\n```text\n{value}\n```\n\n")

        f.write("## Server command\n\n```bash\n")
        f.write(" ".join(server_cmd))
        f.write("\n```\n\n")

        f.write("## Group response summary\n\n")
        f.write("| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |\n")
        f.write("|---|---:|---:|---:|---:|\n")
        for row in group_results:
            f.write(
                f"| {row['file']} "
                f"| {row['active_slots']} "
                f"| {row['group_prompt_tokens']} "
                f"| {fmt(row['group_wall_ms'] / 1000.0)} "
                f"| {fmt(row['group_response_tok_s'])} |\n"
            )

        f.write("\n## Per-request server prefill timings\n\n")
        f.write("| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|\n")
        for row in results:
            f.write(
                f"| {row['file']} "
                f"| {row['active_slots']} "
                f"| {row['request_index']} "
                f"| {row['prompt_tokens']} "
                f"| {fmt(row['prefill_tps'])} "
                f"| {fmt(row['prefill_ms'] / 1000.0)} "
                f"| {fmt(row['wall_ms'] / 1000.0)} |\n"
            )

        f.write("\n## GPU load during group response window\n\n")
        for row in group_results:
            f.write(f"### {row['file']} | active_slots={row['active_slots']}\n\n")
            f.write("| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |\n")
            f.write("|---:|---|---|---:|---:|---:|---:|---:|\n")
            for gpu, sample in row["gpu"].items():
                f.write(
                    f"| {gpu} | {sample['name']} | {sample['pcie']} "
                    f"| {fmt(sample['util_avg'], 1)} | {fmt(sample['util_max'], 1)} "
                    f"| {fmt(sample['power_avg'], 1)} | {fmt(sample['power_max'], 1)} "
                    f"| {fmt(sample['mem_max'], 0)} |\n"
                )
            f.write("\n")

        f.write("\n## Notes\n\n")
        f.write("- `*` values are computed by the benchmark script, not reported by llama-server.\n")
        f.write("- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.\n")
        f.write("- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.\n")
        f.write("- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.\n")
        f.write("- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.\n")


def main():
    out_dir = Path(cfg["OUTPUT_DIR"]) / datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir.mkdir(parents=True, exist_ok=True)

    report = out_dir / "report.md"
    raw_csv = out_dir / "raw_results.csv"
    group_csv = out_dir / "group_results.csv"
    env_info = collect_environment()

    server, server_log, server_cmd = start_server(out_dir)

    ctx_files = sorted(Path(cfg["CONTEXTS_DIR"]).glob("ctx_*.txt"), key=prompt_size_from_name)
    if not ctx_files:
        server.send_signal(signal.SIGINT)
        raise RuntimeError(f"No ctx_*.txt files found in {cfg['CONTEXTS_DIR']}")

    active_slots = int(cfg["PARALLEL"])
    if active_slots < 1:
        server.send_signal(signal.SIGINT)
        raise RuntimeError(f"PARALLEL must be >= 1, got {active_slots}")

    results = []
    group_results = []
    url = f"http://{cfg['HOST']}:{cfg['PORT']}/completion"

    try:
        for ctx in ctx_files:
            text = ctx.read_text(encoding="utf-8", errors="ignore")
            payload = make_payload(text)

            monitor = Monitor(cfg["MONITOR_INTERVAL"])
            monitor.start()

            group_start, group_end, batch_results = request_many_prepared(url, payload, active_slots)

            monitor.stop()
            monitor_samples = monitor.samples

            ctx_rows = []
            for req_i, (t0, t1, data) in enumerate(batch_results, start=1):
                row = row_from_response(ctx, active_slots, req_i, t0, t1, data, monitor_samples)
                results.append(row)
                ctx_rows.append(row)

                print(
                    f"{ctx.name} slots={active_slots} req={req_i}: "
                    f"prefill={row['prefill_tps']:.2f} tok/s "
                    f"wall={row['wall_ms'] / 1000.0:.2f} s"
                )

            grow = group_row_from_results(ctx, active_slots, group_start, group_end, ctx_rows, monitor_samples)
            group_results.append(grow)
            print(
                f"{ctx.name} GROUP slots={active_slots}: "
                f"tokens={grow['group_prompt_tokens']} "
                f"wall*={grow['group_wall_ms'] / 1000.0:.2f} s "
                f"response*={grow['group_response_tok_s']:.2f} tok/s"
            )

    finally:
        try:
            server.send_signal(signal.SIGINT)
        except Exception:
            pass

    write_report(report, raw_csv, group_csv, results, group_results, server_log, server_cmd, env_info)

    print("REPORT:", report)
    print("CSV:", raw_csv)
    print("GROUP CSV:", group_csv)


if __name__ == "__main__":
    main()
