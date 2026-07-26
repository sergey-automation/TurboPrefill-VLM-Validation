# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q8_0.gguf`
- NGL: `999`
- CTX_SIZE: `262000`
- N_GEN: `128`
- BATCH: `4097`
- UBATCH: `32`
- CTK: `f16`
- SPEC_TYPE: `draft-mtp`
- SPEC_DRAFT_N_MAX: `4`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `4/7/7/7/7/7/7/3`
- PARALLEL: `1`
- TEMPERATURE: `0.15`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP_Qwen3.6-35B-A3B-Q8/20260726_193500/llama_server.log`

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
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q8_0.gguf --mmproj /mnt/models/AI/LLM/mmproj-Qwen_Qwen3.6-35B-A3B-f16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 262000 --override-kv llama.context_length=int:262000 -b 4097 -ub 32 -np 1 -ctk f16 -sm layer -ts 4/7/7/7/7/7/7/3 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 128 | 66.45 | 4.03 | 27.61 | 4.64 | 9.00 |
| ctx_000512.txt | 1 | 1 | 541 | 128 | 252.76 | 2.14 | 31.67 | 4.04 | 6.79 |
| ctx_001024.txt | 1 | 1 | 1082 | 128 | 344.45 | 3.14 | 31.63 | 4.05 | 7.88 |
| ctx_002048.txt | 1 | 1 | 2330 | 128 | 329.96 | 7.06 | 42.77 | 2.99 | 10.89 |
| ctx_004096.txt | 1 | 1 | 4288 | 128 | 859.37 | 4.99 | 40.23 | 3.18 | 9.08 |
| ctx_008192.txt | 1 | 1 | 8853 | 128 | 961.03 | 9.21 | 40.74 | 3.14 | 13.40 |
| ctx_016384.txt | 1 | 1 | 17670 | 128 | 913.78 | 19.34 | 38.69 | 3.31 | 24.28 |
| ctx_032768.txt | 1 | 1 | 33613 | 128 | 914.75 | 36.75 | 31.72 | 4.04 | 43.81 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 5251 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 5877 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 6369 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 5877 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 6369 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.8 | 40.8 | 5877 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6369 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2069 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.7 | 10.7 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.3 | 43.3 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.6 | 43.6 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.6 | 44.6 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 48.1 | 48.1 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.0 | 50.0 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.7 | 51.7 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.9 | 53.9 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.4 | 8.4 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.6 | 52.6 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 49.9 | 49.9 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.7 | 50.7 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.6 | 10.6 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.2 | 51.2 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.2 | 50.2 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.7 | 50.7 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.0 | 54.0 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.7 | 45.7 | 5267 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 5893 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 6385 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 5893 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.4 | 42.4 | 6385 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.9 | 45.9 | 5893 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.1 | 54.1 | 6385 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2081 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.6 | 10.6 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.2 | 51.2 | 5267 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.4 | 52.4 | 5893 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.3 | 50.3 | 6385 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 5893 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 6385 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 5893 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.1 | 54.1 | 6385 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.0 | 51.0 | 2081 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 5267 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.5 | 52.5 | 5893 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.2 | 50.2 | 6385 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 5893 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.8 | 52.8 | 6385 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.0 | 41.0 | 5893 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.2 | 54.2 | 6385 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.0 | 51.0 | 2081 |
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

