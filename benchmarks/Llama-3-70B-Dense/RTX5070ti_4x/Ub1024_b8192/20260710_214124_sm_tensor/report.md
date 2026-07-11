# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_214124/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 1024 -np 1 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 340.88 | 0.84 | 22.23 | 5.76 | 6.60 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 413.61 | 1.34 | 22.16 | 5.78 | 7.25 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 436.14 | 2.59 | 21.97 | 5.83 | 8.69 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 447.14 | 4.82 | 21.85 | 5.86 | 11.05 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 450.70 | 9.48 | 20.87 | 6.13 | 16.27 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 445.43 | 19.05 | 21.04 | 6.08 | 26.31 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 433.62 | 40.71 | 19.44 | 6.58 | 49.48 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 405.35 | 85.34 | 18.30 | 7.00 | 97.72 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 40.4 | 40.4 | 10926 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 31.4 | 31.4 | 14634 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 38.7 | 38.7 | 14634 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 40.0 | 40.0 | 14634 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 76.1 | 79.7 | 10948 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.6 | 98.0 | 78.9 | 83.8 | 14656 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 81.6 | 85.7 | 14656 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.0 | 98.0 | 86.8 | 91.0 | 14656 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 61.8 | 68.2 | 10970 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 59.4 | 66.6 | 14678 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 51.0 | 100.0 | 63.4 | 69.2 | 14678 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 50.5 | 100.0 | 65.8 | 74.0 | 14678 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.6 | 98.0 | 78.8 | 79.7 | 10970 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 82.0 | 83.8 | 14678 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 84.0 | 85.7 | 14678 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.0 | 98.0 | 89.8 | 91.1 | 14678 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 51.2 | 58.1 | 11004 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 48.0 | 55.9 | 14712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 52.0 | 59.5 | 14712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 66.7 | 100.0 | 52.2 | 61.8 | 14712 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.5 | 98.0 | 78.3 | 80.0 | 11024 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.5 | 98.0 | 82.5 | 84.3 | 14732 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 84.2 | 86.3 | 14732 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.0 | 98.0 | 89.7 | 91.5 | 14732 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 75.0 | 100.0 | 52.1 | 58.5 | 11024 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 75.0 | 100.0 | 48.7 | 56.1 | 14732 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 75.0 | 100.0 | 52.8 | 59.9 | 14732 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 75.0 | 100.0 | 54.6 | 62.1 | 14732 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 95.6 | 98.0 | 75.0 | 80.2 | 11024 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.0 | 98.0 | 77.3 | 84.3 | 14732 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 96.8 | 98.0 | 81.0 | 86.5 | 14732 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 95.2 | 98.0 | 85.3 | 91.9 | 14732 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 55.4 | 59.4 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 52.2 | 57.1 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.9 | 100.0 | 55.7 | 60.5 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 88.9 | 100.0 | 57.8 | 62.9 | 14734 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.0 | 98.0 | 76.6 | 80.6 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 80.4 | 85.1 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 97.8 | 98.0 | 82.3 | 86.8 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 97.7 | 98.0 | 87.2 | 92.2 | 14734 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.5 | 100.0 | 56.7 | 59.5 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 87.0 | 100.0 | 54.3 | 58.8 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 86.9 | 100.0 | 57.6 | 61.7 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 87.2 | 100.0 | 59.5 | 64.1 | 14734 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 74.7 | 78.9 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 78.6 | 84.1 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 80.7 | 85.5 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.3 | 100.0 | 85.6 | 90.9 | 14734 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 89.5 | 100.0 | 57.7 | 59.7 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 89.8 | 100.0 | 57.0 | 60.5 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 89.6 | 100.0 | 59.9 | 63.2 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 90.7 | 100.0 | 62.5 | 66.8 | 14734 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 96.4 | 100.0 | 71.0 | 77.7 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 88.4 | 100.0 | 75.2 | 83.8 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 87.9 | 100.0 | 77.0 | 85.2 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 89.7 | 100.0 | 82.2 | 90.8 | 14734 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 93.5 | 100.0 | 58.1 | 67.5 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 92.4 | 100.0 | 58.5 | 71.3 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 92.2 | 100.0 | 61.6 | 73.2 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 92.3 | 100.0 | 64.3 | 77.1 | 14734 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 94.3 | 100.0 | 68.9 | 77.0 | 11026 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 96.3 | 100.0 | 74.4 | 84.0 | 14734 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 98.3 | 100.0 | 76.9 | 85.7 | 14734 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 98.6 | 100.0 | 80.9 | 90.9 | 14734 |

