# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen3.6-27B/Qwen3.6-27B-MTP-Q8_0.gguf`
- NGL: `999`
- CTX_SIZE: `131072`
- N_GEN: `64`
- BATCH: `4096`
- UBATCH: `32`
- CTK: `f16`
- SPEC_TYPE: `draft-mtp`
- SPEC_DRAFT_N_MAX: `4`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `1/4/5/5/5/5/5/5/5/5/5/5/5/4/1`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP/20260725_184307/llama_server.log`

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
/home/serg/workspace/versions/TurboPrefill-MTP/build/bin/llama-server
```

### LOCAL_LD_LIBRARY_PATH

```text
/home/serg/workspace/versions/TurboPrefill-MTP/build/bin
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
/home/serg/workspace/versions/TurboPrefill-MTP/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen3.6-27B/Qwen3.6-27B-MTP-Q8_0.gguf --mmproj /mnt/models/AI/LLM/Qwen3.6-27B/mmproj-F16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 131072 --override-kv llama.context_length=int:131072 -b 4096 -ub 32 -np 1 -ctk f16 -sm layer -ts 1/4/5/5/5/5/5/5/5/5/5/5/5/4/1 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 64 | 31.45 | 8.52 | 11.36 | 5.63 | 14.47 |
| ctx_000512.txt | 1 | 1 | 541 | 64 | 114.75 | 4.71 | 14.29 | 4.48 | 10.36 |
| ctx_001024.txt | 1 | 1 | 1082 | 64 | 159.90 | 6.77 | 13.30 | 4.81 | 12.89 |
| ctx_002048.txt | 1 | 1 | 2330 | 64 | 164.11 | 14.20 | 10.33 | 6.19 | 21.95 |
| ctx_004096.txt | 1 | 1 | 4288 | 64 | 198.22 | 21.63 | 9.97 | 6.42 | 30.00 |
| ctx_008192.txt | 1 | 1 | 8853 | 64 | 203.17 | 43.57 | 14.27 | 4.48 | 50.67 |
| ctx_016384.txt | 1 | 1 | 17670 | 64 | 192.59 | 91.75 | 9.59 | 6.67 | 102.65 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.1 | 50.1 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.9 | 42.9 | 2261 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 2665 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 3149 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 2665 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.4 | 40.4 | 2665 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 2665 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 3149 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 2665 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.8 | 42.8 | 2665 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 2665 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 3149 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.2 | 41.2 | 2665 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 2847 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.4 | 45.4 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.4 | 40.4 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.9 | 51.9 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.7 | 52.7 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.7 | 43.7 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.3 | 45.3 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 47.3 | 47.3 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.3 | 52.3 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.7 | 53.7 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.5 | 51.5 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.7 | 52.7 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.3 | 53.3 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.5 | 49.5 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.4 | 51.4 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.0 | 50.0 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.3 | 52.3 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.7 | 53.7 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.7 | 53.7 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.3 | 51.3 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.7 | 43.7 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.3 | 44.3 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.3 | 52.3 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.2 | 53.2 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.7 | 49.7 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.9 | 52.9 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.5 | 53.5 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.0 | 52.0 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.5 | 53.5 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.1 | 50.1 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.0 | 52.0 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.4 | 51.4 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.1 | 44.1 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.6 | 53.6 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.2 | 44.2 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.9 | 42.9 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.2 | 41.2 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.6 | 54.6 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.4 | 42.4 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.4 | 53.4 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.0 | 53.0 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.1 | 44.1 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.0 | 44.0 | 1407 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 3.0 | 3.0 | 42.3 | 42.3 | 2071 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 8.0 | 54.2 | 54.2 | 2263 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 8.0 | 42.3 | 42.3 | 2667 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 12.0 | 12.0 | 44.2 | 44.2 | 3151 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.1 | 53.1 | 2667 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 41.7 | 41.7 | 2667 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 45.5 | 45.5 | 2667 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 43.5 | 43.5 | 3151 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 57.3 | 57.3 | 2667 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 61.5 | 61.5 | 2667 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 59.1 | 59.1 | 2667 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 92.9 | 92.9 | 3151 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 1.0 | 1.0 | 102.6 | 102.6 | 2667 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 19.0 | 19.0 | 42.0 | 42.0 | 2851 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 8.0 | 44.3 | 44.3 | 1407 |

