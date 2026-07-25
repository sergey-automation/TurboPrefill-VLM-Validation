# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen3.6-27B/Qwen3.6-27B-MTP-Q8_0.gguf`
- NGL: `999`
- CTX_SIZE: `131072`
- N_GEN: `64`
- BATCH: `4097`
- UBATCH: `32`
- CTK: `f16`
- SPEC_TYPE: `draft-mtp`
- SPEC_DRAFT_N_MAX: `4`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `4/8/8/8/8/8/8/5`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP/20260725_204736/llama_server.log`

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
/home/serg/workspace/versions/TurboPrefill-MTP/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen3.6-27B/Qwen3.6-27B-MTP-Q8_0.gguf --mmproj /mnt/models/AI/LLM/Qwen3.6-27B/mmproj-F16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 131072 --override-kv llama.context_length=int:131072 -b 4097 -ub 32 -np 1 -ctk f16 -sm layer -ts 4/8/8/8/8/8/8/5 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 64 | 41.83 | 6.41 | 11.89 | 5.38 | 12.14 |
| ctx_000512.txt | 1 | 1 | 541 | 64 | 128.17 | 4.22 | 14.76 | 4.34 | 9.73 |
| ctx_001024.txt | 1 | 1 | 1082 | 64 | 172.53 | 6.27 | 13.63 | 4.70 | 12.29 |
| ctx_002048.txt | 1 | 1 | 2330 | 64 | 169.12 | 13.78 | 11.65 | 5.49 | 20.84 |
| ctx_004096.txt | 1 | 1 | 4288 | 64 | 204.13 | 21.01 | 11.36 | 5.63 | 28.60 |
| ctx_008192.txt | 1 | 1 | 8853 | 64 | 214.34 | 41.30 | 15.46 | 4.14 | 48.04 |
| ctx_016384.txt | 1 | 1 | 17670 | 64 | 199.79 | 88.44 | 11.66 | 5.49 | 98.25 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.0 | 50.0 | 3801 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 4767 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 5655 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 4767 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 4767 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.4 | 40.4 | 4767 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 5655 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 4139 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.4 | 45.4 | 3803 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 4769 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 5657 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.7 | 43.7 | 4769 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 4769 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 4769 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.7 | 52.7 | 5657 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 4141 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.1 | 9.1 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.3 | 8.3 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 3803 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 4769 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 5657 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.4 | 52.4 | 4769 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 4769 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 4769 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.7 | 52.7 | 5657 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 4141 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 3803 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 4769 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.4 | 49.4 | 5657 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 4769 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 4769 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.6 | 50.6 | 4769 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.3 | 44.3 | 5657 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 4141 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.2 | 51.2 | 3803 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 4769 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 5657 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 4769 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.5 | 42.5 | 4769 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 4769 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.2 | 53.2 | 5657 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 4141 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 11.0 | 11.0 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.6 | 9.6 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.6 | 8.6 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 3803 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.2 | 53.2 | 4769 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.7 | 49.7 | 5657 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 4769 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.9 | 52.9 | 4769 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.2 | 51.2 | 4769 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.6 | 44.6 | 5657 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 4141 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 3803 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.0 | 54.0 | 4769 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.6 | 50.6 | 5657 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.9 | 52.9 | 4769 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.2 | 53.2 | 4769 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.4 | 51.4 | 4769 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.0 | 54.0 | 5657 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.5 | 50.5 | 4141 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

