# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen3.6-35B-A3B-bf16/Qwen_Qwen3.6-35B-A3B-bf16-00001-of-00002.gguf`
- NGL: `999`
- CTX_SIZE: `131072`
- N_GEN: `64`
- BATCH: `4097`
- UBATCH: `32`
- CTK: `f16`
- SPEC_TYPE: `draft-mtp`
- SPEC_DRAFT_N_MAX: `4`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `1/3/3/3/3/3/3/3/3/3/3/3/3/3/1`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP_Qwen3.6-35B-A3B-f16/20260726_113820/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
```

### SCRIPT_DIR

```text
/home/serg/workspace/versions/TurboPrefill_b10068
```

### LLAMA_SERVER_BIN

```text
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin/llama-server
```

### LOCAL_LD_LIBRARY_PATH

```text
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin
```

### nvidia_smi

```text
0, NVIDIA P104-100, 535.309.01, 8192 MiB
1, NVIDIA P104-100, 535.309.01, 8192 MiB
2, NVIDIA P104-100, 535.309.01, 8192 MiB
3, NVIDIA P104-100, 535.309.01, 8192 MiB
4, NVIDIA P104-100, 535.309.01, 8192 MiB
5, NVIDIA P104-100, 535.309.01, 8192 MiB
6, NVIDIA P104-100, 535.309.01, 8192 MiB
7, NVIDIA P104-100, 535.309.01, 8192 MiB
8, NVIDIA P104-100, 535.309.01, 8192 MiB
9, NVIDIA P104-100, 535.309.01, 8192 MiB
10, NVIDIA P104-100, 535.309.01, 8192 MiB
11, NVIDIA P104-100, 535.309.01, 8192 MiB
12, NVIDIA P104-100, 535.309.01, 8192 MiB
13, NVIDIA P104-100, 535.309.01, 8192 MiB
14, NVIDIA P104-100, 535.309.01, 8192 MiB
```

### nvcc

```text
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0
```

### cmake

```text
cmake version 3.28.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

## Server command

```bash
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen3.6-35B-A3B-bf16/Qwen_Qwen3.6-35B-A3B-bf16-00001-of-00002.gguf --mmproj /mnt/models/AI/LLM/mmproj-Qwen_Qwen3.6-35B-A3B-f16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 131072 --override-kv llama.context_length=int:131072 -b 4097 -ub 32 -np 1 -ctk f16 -sm layer -ts 1/3/3/3/3/3/3/3/3/3/3/3/3/3/1 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 64 | 18.81 | 14.25 | 8.26 | 7.75 | 22.42 |
| ctx_000512.txt | 1 | 1 | 541 | 64 | 27.84 | 19.43 | 8.41 | 7.61 | 27.65 |
| ctx_001024.txt | 1 | 1 | 1082 | 64 | 28.25 | 38.30 | 7.93 | 8.07 | 47.09 |
| ctx_002048.txt | 1 | 1 | 2330 | 64 | 28.01 | 83.19 | 13.15 | 4.87 | 88.90 |
| ctx_004096.txt | 1 | 1 | 4288 | 64 | 258.27 | 16.60 | 13.74 | 4.66 | 22.19 |
| ctx_008192.txt | 1 | 1 | 8853 | 64 | 212.11 | 41.74 | 12.91 | 4.96 | 47.76 |
| ctx_016384.txt | 1 | 1 | 17670 | 64 | 204.67 | 86.33 | 12.79 | 5.01 | 92.95 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.0 | 50.0 | 4469 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.9 | 42.9 | 5245 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 5245 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 4979 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 5245 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.4 | 40.4 | 5245 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 5245 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 4979 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 5245 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 5245 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 5245 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 4979 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.2 | 41.2 | 5245 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 5541 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 4471 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 5249 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 5249 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 47.6 | 47.6 | 4981 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.2 | 44.2 | 5249 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 47.0 | 47.0 | 5249 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 5249 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.6 | 45.6 | 4981 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 46.1 | 46.1 | 5249 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.2 | 52.2 | 5249 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.7 | 52.7 | 5249 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 4981 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 5249 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 5549 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 4471 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.8 | 52.8 | 5249 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 5249 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 4981 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 5249 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 5249 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.8 | 53.8 | 5249 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 4981 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.4 | 52.4 | 5249 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.3 | 52.3 | 5249 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 5249 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.8 | 49.8 | 4981 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 5249 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 5549 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.7 | 43.7 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 4471 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.2 | 52.2 | 5249 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.8 | 45.8 | 5249 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 4981 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.4 | 52.4 | 5249 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.6 | 50.6 | 5249 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 5249 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 4981 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.0 | 52.0 | 5249 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.6 | 50.6 | 5249 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 48.7 | 48.7 | 5249 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.0 | 41.0 | 4981 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 5249 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.2 | 51.2 | 5549 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.5 | 51.5 | 4471 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.0 | 53.0 | 5249 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.8 | 49.8 | 5249 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 48.3 | 48.3 | 4981 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.0 | 53.0 | 5249 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 5249 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.8 | 53.8 | 5249 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 46.4 | 46.4 | 4981 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 46.9 | 46.9 | 5249 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.2 | 49.2 | 5249 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.0 | 44.0 | 5249 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.2 | 41.2 | 4981 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 5249 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.3 | 51.3 | 5549 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.1 | 44.1 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.5 | 51.5 | 4471 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.1 | 53.1 | 5251 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.1 | 50.1 | 5251 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.2 | 52.2 | 4981 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.9 | 42.9 | 5251 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.3 | 51.3 | 5251 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.8 | 53.8 | 5251 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 4981 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 5251 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.8 | 52.8 | 5251 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.6 | 54.6 | 5251 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.6 | 49.6 | 4981 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 5251 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 5553 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.0 | 44.0 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 4471 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.1 | 53.1 | 5251 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.0 | 50.0 | 5251 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.2 | 52.2 | 4981 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.9 | 42.9 | 5251 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.5 | 51.5 | 5251 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 48.6 | 48.6 | 5251 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.4 | 51.4 | 4981 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 5251 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.0 | 53.0 | 5251 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.6 | 54.6 | 5251 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 4981 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 5251 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.9 | 41.9 | 5553 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.0 | 44.0 | 1081 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

