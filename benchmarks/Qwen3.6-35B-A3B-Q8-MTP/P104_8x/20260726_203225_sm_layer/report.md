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
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/versions/TurboPrefill_b10068/bench_reports_MTP_Qwen3.6-35B-A3B-Q8/20260726_203225/llama_server.log`

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
/home/serg/workspace/versions/TurboPrefill_b10068/build/bin/llama-server -m /mnt/models/AI/LLM/Qwen_Qwen3.6-35B-A3B-Q8_0.gguf --mmproj /mnt/models/AI/LLM/mmproj-Qwen_Qwen3.6-35B-A3B-f16.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 999 -c 262000 --override-kv llama.context_length=int:262000 -b 4097 -ub 32 -np 1 -ctk f16 -sm layer -ts 4/7/7/7/7/7/7/3 --spec-type draft-mtp --spec-draft-n-max 4
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 268 | 128 | 57.06 | 4.70 | 31.78 | 4.03 | 9.08 |
| ctx_000512.txt | 1 | 1 | 541 | 128 | 165.33 | 3.27 | 33.56 | 3.81 | 7.68 |
| ctx_001024.txt | 1 | 1 | 1082 | 128 | 173.72 | 6.23 | 28.92 | 4.43 | 11.37 |
| ctx_002048.txt | 1 | 1 | 2330 | 128 | 181.24 | 12.86 | 41.36 | 3.09 | 16.75 |
| ctx_004096.txt | 1 | 1 | 4288 | 128 | 186.35 | 23.01 | 32.23 | 3.97 | 27.89 |
| ctx_008192.txt | 1 | 1 | 8853 | 128 | 182.59 | 48.49 | 37.00 | 3.46 | 53.00 |
| ctx_016384.txt | 1 | 1 | 17670 | 128 | 174.70 | 101.14 | 33.22 | 3.85 | 106.64 |
| ctx_032768.txt | 1 | 1 | 33613 | 1 | 163.44 | 205.65 | 1000000.00 | 0.00 | 208.63 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.4 | 50.4 | 5251 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.0 | 43.0 | 5877 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 6369 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.7 | 43.7 | 5877 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 6369 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 5877 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6369 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.1 | 42.1 | 2069 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 9.1 | 9.1 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.2 | 42.2 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.7 | 50.7 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.2 | 10.2 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.4 | 41.4 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.8 | 40.8 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.2 | 44.2 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.5 | 8.5 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.6 | 41.6 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.7 | 40.7 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2079 |
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

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.7 | 41.7 | 5265 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.2 | 43.2 | 5891 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.5 | 41.5 | 6383 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.0 | 51.0 | 5891 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.8 | 51.8 | 6383 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 5891 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6383 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.8 | 50.8 | 2079 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.1 | 10.1 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 5267 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.5 | 43.5 | 5893 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.8 | 41.8 | 6385 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.9 | 43.9 | 5893 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.5 | 42.5 | 6385 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 40.9 | 40.9 | 5893 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.2 | 44.2 | 6385 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.9 | 50.9 | 2081 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.8 | 8.8 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.5 | 10.5 | 89 |
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
| 0 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 42.3 | 42.3 | 5267 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 43.8 | 43.8 | 5893 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.6 | 44.6 | 6385 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.2 | 44.2 | 5893 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 46.3 | 46.3 | 6385 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.0 | 41.0 | 5893 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.4 | 44.4 | 6385 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 2081 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
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
| 1 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.1 | 44.1 | 5893 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 50.5 | 50.5 | 6385 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 52.1 | 52.1 | 5893 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 53.0 | 53.0 | 6385 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 41.3 | 41.3 | 5893 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 54.2 | 54.2 | 6385 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 51.1 | 51.1 | 2081 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.7 | 8.7 | 89 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.4 | 10.4 | 89 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.2 | 8.2 | 89 |
| 12 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 13 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 8.9 | 8.9 | 89 |
| 14 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 10.3 | 10.3 | 89 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

