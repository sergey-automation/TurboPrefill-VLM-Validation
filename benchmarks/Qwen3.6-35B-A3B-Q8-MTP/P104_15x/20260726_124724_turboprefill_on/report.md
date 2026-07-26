# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q8_0.gguf`
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
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP_Qwen3.6-35B-A3B-Q8/20260726_124724/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
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
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q8_0.gguf --mmproj /mnt/models/AI/LLM/mmproj-Qwen_Qwen3.6-35B-A3B-f16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 131072 --override-kv llama.context_length=int:131072 -b 4097 -ub 32 -np 1 -ctk f16 -sm layer -ts 1/3/3/3/3/3/3/3/3/3/3/3/3/3/1 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 64 | 50.71 | 5.29 | 30.23 | 2.12 | 7.73 |
| ctx_000512.txt | 1 | 1 | 541 | 64 | 153.89 | 3.52 | 29.34 | 2.18 | 6.30 |
| ctx_001024.txt | 1 | 1 | 1082 | 64 | 163.67 | 6.61 | 24.03 | 2.66 | 9.97 |
| ctx_002048.txt | 1 | 1 | 2330 | 64 | 160.55 | 14.51 | 38.45 | 1.66 | 17.03 |
| ctx_004096.txt | 1 | 1 | 4288 | 64 | 172.67 | 24.83 | 29.82 | 2.15 | 27.87 |
| ctx_008192.txt | 1 | 1 | 8853 | 64 | 170.65 | 51.88 | 33.00 | 1.94 | 54.90 |
| ctx_016384.txt | 1 | 1 | 17670 | 64 | 159.02 | 111.12 | 28.39 | 2.25 | 115.00 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.1 | 50.1 | 2959 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 2989 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 2989 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 2717 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 2989 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.5 | 40.5 | 2989 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 2989 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2717 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 2989 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.8 | 42.8 | 2989 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 2989 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 2717 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 2989 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 3275 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 2969 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 3003 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 3003 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 2727 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 3003 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.5 | 40.5 | 3003 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 3003 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2727 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 3003 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 3003 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.9 | 42.9 | 3003 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 2727 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.2 | 41.2 | 3003 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 3301 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.4 | 52.4 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 2969 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 3003 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 3003 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 2727 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 3003 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.8 | 40.8 | 3003 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 3003 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 2727 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 3003 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 3003 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 3003 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 2727 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.2 | 41.2 | 3003 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 47.4 | 47.4 | 3301 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.9 | 52.9 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 2969 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 3003 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 3003 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 2727 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 3003 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.6 | 40.6 | 3003 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 3003 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2727 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 3003 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 3003 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 3003 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 2727 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 3003 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 3301 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.2 | 53.2 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 2969 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 3003 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 3003 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 2727 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 3003 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 3003 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 3003 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2727 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.0 | 42.0 | 3003 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 3003 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 3003 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 2727 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 3003 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 3301 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.1 | 53.1 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 2969 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 3005 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 3005 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 2727 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 3005 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 3005 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 3005 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.4 | 42.4 | 2727 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 3005 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 3005 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 3005 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.0 | 41.0 | 2727 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.9 | 41.9 | 3005 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 3305 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 48.3 | 48.3 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 2969 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 3005 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 3005 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 2727 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.6 | 42.6 | 3005 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 3005 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 3005 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.4 | 42.4 | 2727 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.4 | 42.4 | 3005 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.1 | 43.1 | 3005 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 3005 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.0 | 41.0 | 2727 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 3005 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.5 | 51.5 | 3305 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.5 | 53.5 | 633 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

