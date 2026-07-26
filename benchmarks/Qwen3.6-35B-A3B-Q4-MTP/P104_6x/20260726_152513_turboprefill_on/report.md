# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q4_K_L.gguf`
- NGL: `999`
- CTX_SIZE: `131072`
- N_GEN: `64`
- BATCH: `2048`
- UBATCH: `32`
- CTK: `f16`
- SPEC_TYPE: `draft-mtp`
- SPEC_DRAFT_N_MAX: `4`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `5/8/8/8/8/4`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP_Qwen3.6-35B-A3B-Q4/20260726_152513/llama_server.log`

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
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q4_K_L.gguf --mmproj /mnt/models/AI/LLM/mmproj-Qwen_Qwen3.6-35B-A3B-f16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 131072 --override-kv llama.context_length=int:131072 -b 2048 -ub 32 -np 1 -ctk f16 -sm layer -ts 5/8/8/8/8/4 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 1 | 56.99 | 4.70 | 1000000.00 | 0.00 | 5.04 |
| ctx_000512.txt | 1 | 1 | 541 | 64 | 214.84 | 2.52 | 26.31 | 2.43 | 5.53 |
| ctx_001024.txt | 1 | 1 | 1082 | 64 | 321.13 | 3.37 | 31.02 | 2.06 | 6.10 |
| ctx_002048.txt | 1 | 1 | 2330 | 64 | 302.40 | 7.71 | 42.13 | 1.52 | 10.04 |
| ctx_004096.txt | 1 | 1 | 4288 | 64 | 399.91 | 10.72 | 30.11 | 2.13 | 13.74 |
| ctx_008192.txt | 1 | 1 | 8853 | 64 | 405.26 | 21.85 | 18.29 | 3.50 | 26.38 |
| ctx_016384.txt | 1 | 1 | 17670 | 64 | 390.09 | 45.30 | 29.04 | 2.20 | 49.12 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 4667 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 4595 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 4533 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 4599 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.4 | 42.4 | 4737 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 3143 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.8 | 9.8 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 4681 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 4609 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 4547 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.2 | 52.2 | 4613 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 4751 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 3165 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.8 | 9.8 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 4681 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 4609 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 4547 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 4613 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 4751 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 3165 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.8 | 9.8 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 4681 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 4609 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 4547 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.9 | 51.9 | 4613 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 4751 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.7 | 50.7 | 3165 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.9 | 9.9 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.5 | 9.5 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 4681 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.0 | 52.0 | 4609 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.4 | 49.4 | 4547 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.0 | 52.0 | 4613 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 4751 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.7 | 50.7 | 3165 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.8 | 9.8 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.1 | 9.1 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.6 | 8.6 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 4683 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.7 | 43.7 | 4611 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 4549 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.2 | 44.2 | 4615 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 4753 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 3169 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.8 | 9.8 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.5 | 51.5 | 4683 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.8 | 52.8 | 4611 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.0 | 50.0 | 4549 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 4615 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.5 | 42.5 | 4753 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.4 | 51.4 | 3169 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.7 | 9.7 | 89 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

