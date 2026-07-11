# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `512`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_213716/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
```

### nvidia_smi

```text
0, NVIDIA GeForce RTX 5070 Ti, 580.126.09, 16303 MiB
1, NVIDIA GeForce RTX 5070 Ti, 580.126.09, 16303 MiB
2, NVIDIA GeForce RTX 5070 Ti, 580.126.09, 16303 MiB
3, NVIDIA GeForce RTX 5070 Ti, 580.126.09, 16303 MiB
```

### nvcc

```text
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:58:59_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```

### cmake

```text
cmake version 3.28.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

## Server command

```bash
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 512 -np 1 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 356.79 | 0.80 | 22.25 | 5.75 | 6.56 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 438.72 | 1.27 | 22.14 | 5.78 | 7.18 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 434.88 | 2.60 | 22.14 | 5.78 | 8.60 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 444.33 | 4.85 | 21.78 | 5.88 | 11.10 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 448.10 | 9.54 | 20.88 | 6.13 | 16.33 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 443.15 | 19.15 | 21.02 | 6.09 | 26.41 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 429.57 | 41.09 | 19.57 | 6.54 | 49.83 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 401.32 | 86.20 | 18.26 | 7.01 | 97.91 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 40.8 | 40.8 | 10674 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 31.4 | 31.4 | 14382 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 36.7 | 36.7 | 14382 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 39.0 | 39.0 | 14382 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 75.6 | 78.3 | 10696 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 79.9 | 83.8 | 14404 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 82.2 | 85.7 | 14404 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.0 | 98.0 | 86.2 | 90.8 | 14404 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 65.9 | 65.9 | 10696 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 1.0 | 1.0 | 61.4 | 61.4 | 14404 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 2.0 | 2.0 | 64.3 | 64.3 | 14404 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 1.0 | 1.0 | 70.4 | 70.4 | 14404 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.2 | 100.0 | 74.1 | 78.6 | 10734 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.2 | 100.0 | 78.3 | 84.0 | 14442 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.2 | 100.0 | 80.4 | 86.2 | 14442 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.0 | 100.0 | 85.0 | 91.4 | 14442 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 50.5 | 57.3 | 10734 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 46.2 | 55.8 | 14442 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 52.7 | 59.5 | 14442 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 66.7 | 100.0 | 54.6 | 61.6 | 14442 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 77.4 | 78.7 | 10734 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 82.7 | 84.0 | 14442 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 85.0 | 86.2 | 14442 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.0 | 98.0 | 89.3 | 91.2 | 14442 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 80.0 | 100.0 | 52.5 | 57.3 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 79.8 | 100.0 | 49.6 | 56.2 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 80.0 | 100.0 | 53.5 | 59.7 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 79.6 | 100.0 | 55.4 | 61.9 | 14446 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.4 | 98.0 | 76.5 | 78.4 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.0 | 98.0 | 81.7 | 84.2 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.4 | 98.0 | 84.5 | 86.2 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 96.8 | 98.0 | 89.2 | 91.4 | 14446 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 56.0 | 57.7 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 54.2 | 56.6 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 57.9 | 60.2 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 88.9 | 100.0 | 60.1 | 62.6 | 14446 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 94.0 | 98.0 | 74.8 | 78.8 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 94.2 | 98.0 | 78.9 | 84.4 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 94.2 | 98.0 | 81.3 | 86.5 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 94.2 | 98.0 | 86.4 | 91.9 | 14446 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 87.4 | 100.0 | 55.6 | 58.0 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 85.9 | 100.0 | 54.1 | 57.8 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 86.1 | 100.0 | 57.6 | 61.2 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 87.1 | 100.0 | 59.6 | 63.5 | 14446 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.7 | 98.0 | 72.7 | 78.0 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 95.5 | 98.0 | 76.6 | 83.4 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 95.5 | 98.0 | 79.2 | 85.6 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 95.3 | 98.0 | 84.2 | 91.0 | 14446 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 90.8 | 100.0 | 57.6 | 74.7 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 90.6 | 100.0 | 56.8 | 75.0 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 90.6 | 100.0 | 60.4 | 77.4 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 89.8 | 100.0 | 62.8 | 82.7 | 14446 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 96.4 | 100.0 | 71.7 | 78.2 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.5 | 100.0 | 75.0 | 83.4 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.5 | 100.0 | 77.8 | 85.3 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.4 | 100.0 | 82.2 | 90.9 | 14446 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 92.5 | 100.0 | 57.8 | 60.9 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 91.3 | 100.0 | 57.8 | 64.9 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 91.3 | 100.0 | 61.3 | 67.7 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 90.9 | 100.0 | 63.8 | 70.7 | 14446 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.9 | 100.0 | 69.4 | 77.8 | 10736 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.5 | 100.0 | 74.4 | 83.7 | 14446 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 76.6 | 85.2 | 14446 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 97.4 | 100.0 | 81.0 | 91.0 | 14446 |

