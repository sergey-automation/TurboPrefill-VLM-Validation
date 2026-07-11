# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `256`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_213255/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 256 -np 1 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 369.69 | 0.77 | 22.31 | 5.74 | 6.52 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 397.92 | 1.39 | 22.35 | 5.73 | 7.25 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 423.94 | 2.67 | 22.20 | 5.77 | 8.65 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 433.62 | 4.97 | 21.89 | 5.85 | 11.18 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 436.90 | 9.78 | 20.87 | 6.13 | 16.64 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 432.27 | 19.63 | 21.23 | 6.03 | 26.81 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 416.86 | 42.34 | 19.51 | 6.56 | 51.12 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 392.25 | 88.19 | 18.31 | 6.99 | 99.90 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 43.4 | 43.4 | 10568 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 36.9 | 36.9 | 14276 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 41.2 | 41.2 | 14276 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 11.0 | 11.0 | 42.6 | 42.6 | 14276 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 76.0 | 78.9 | 10590 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 80.4 | 84.3 | 14298 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 82.4 | 86.2 | 14298 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 97.6 | 98.0 | 87.2 | 91.6 | 14298 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 60.1 | 64.4 | 10590 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 58.7 | 64.4 | 14298 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 62.8 | 68.8 | 14298 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 51.0 | 100.0 | 62.5 | 66.2 | 14298 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 78.0 | 79.1 | 10590 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 83.0 | 84.4 | 14298 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 84.4 | 86.1 | 14298 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 97.8 | 98.0 | 90.5 | 91.4 | 14298 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 51.3 | 58.2 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 48.9 | 56.9 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 51.8 | 60.1 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 66.7 | 100.0 | 55.4 | 62.2 | 14302 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 76.9 | 78.9 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 82.5 | 84.5 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 84.7 | 86.6 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 97.8 | 98.0 | 90.2 | 91.7 | 14302 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 71.6 | 100.0 | 54.2 | 58.5 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 77.0 | 100.0 | 51.2 | 57.2 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 77.2 | 100.0 | 54.9 | 60.3 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 79.2 | 100.0 | 55.7 | 62.8 | 14302 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.6 | 98.0 | 76.0 | 78.8 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 81.0 | 84.6 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 83.2 | 86.8 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 97.8 | 98.0 | 87.7 | 91.6 | 14302 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 57.8 | 66.2 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 56.4 | 67.2 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 60.1 | 71.8 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 88.9 | 100.0 | 62.3 | 74.2 | 14302 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 95.6 | 98.0 | 74.3 | 78.7 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.4 | 100.0 | 77.5 | 84.8 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.4 | 100.0 | 80.6 | 86.9 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.2 | 100.0 | 85.9 | 92.1 | 14302 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.2 | 100.0 | 56.4 | 59.4 | 10594 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 87.5 | 100.0 | 54.9 | 59.1 | 14302 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.4 | 100.0 | 58.4 | 62.6 | 14302 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 88.3 | 100.0 | 60.6 | 64.8 | 14302 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 74.2 | 78.3 | 10596 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 78.9 | 84.1 | 14304 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 81.3 | 86.2 | 14304 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.3 | 100.0 | 85.8 | 91.5 | 14304 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 90.7 | 100.0 | 57.4 | 59.5 | 10596 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 90.1 | 100.0 | 56.6 | 59.9 | 14304 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 91.9 | 100.0 | 60.0 | 63.0 | 14304 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 91.4 | 100.0 | 62.1 | 65.4 | 14304 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 84.6 | 100.0 | 71.1 | 77.5 | 10596 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 95.9 | 100.0 | 75.3 | 83.3 | 14304 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 96.1 | 100.0 | 77.6 | 85.2 | 14304 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 94.1 | 100.0 | 81.7 | 90.4 | 14304 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 92.2 | 100.0 | 58.6 | 72.4 | 10596 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 91.9 | 100.0 | 59.2 | 77.6 | 14304 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 91.6 | 100.0 | 62.6 | 79.4 | 14304 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 91.6 | 100.0 | 64.9 | 84.4 | 14304 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.7 | 100.0 | 69.9 | 77.0 | 10596 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.8 | 100.0 | 75.6 | 83.9 | 14304 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.7 | 100.0 | 78.0 | 85.8 | 14304 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.8 | 100.0 | 82.3 | 91.2 | 14304 |

