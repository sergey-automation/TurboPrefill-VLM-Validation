# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `128`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_202416/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 128 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 392.25 | 0.73 | 9.27 | 13.81 | 14.55 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 592.62 | 0.94 | 9.25 | 13.84 | 14.89 |
| ctx_001024.txt | 1 | 1 | 1131 | 13 | 735.36 | 1.54 | 9.81 | 1.32 | 3.02 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 871.29 | 2.47 | 9.02 | 14.19 | 16.91 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 990.96 | 4.31 | 8.74 | 14.64 | 19.42 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 991.13 | 8.56 | 8.72 | 14.68 | 24.09 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 919.01 | 19.21 | 8.18 | 15.64 | 36.50 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 759.22 | 45.56 | 7.38 | 17.36 | 66.59 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 44.0 | 44.0 | 11880 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 38.1 | 38.1 | 13380 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 42.1 | 42.1 | 13380 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 43.6 | 43.6 | 14014 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.8 | 25.0 | 56.5 | 58.6 | 11880 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.0 | 28.0 | 52.3 | 54.9 | 13386 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.3 | 28.0 | 56.6 | 61.5 | 13386 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 27.2 | 30.0 | 60.5 | 63.4 | 14020 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 49.0 | 49.0 | 11880 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 5.0 | 5.0 | 43.3 | 43.3 | 13386 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 5.0 | 5.0 | 48.1 | 48.1 | 13386 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 2.0 | 2.0 | 50.8 | 50.8 | 14020 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.0 | 25.0 | 57.0 | 65.9 | 11880 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.1 | 28.0 | 53.0 | 65.8 | 13386 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.9 | 28.0 | 57.5 | 65.9 | 13386 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.3 | 29.0 | 60.7 | 69.3 | 14020 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 67.1 | 83.9 | 11880 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 38.5 | 77.0 | 63.1 | 80.7 | 13386 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 47.5 | 95.0 | 64.4 | 79.2 | 13386 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 42.0 | 84.0 | 65.6 | 76.2 | 14020 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.0 | 25.0 | 54.1 | 54.1 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 28.0 | 28.0 | 47.6 | 47.6 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 28.0 | 28.0 | 54.0 | 54.0 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 29.0 | 29.0 | 62.5 | 62.5 | 14022 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.0 | 72.0 | 71.1 | 84.7 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.7 | 83.0 | 69.1 | 85.8 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 57.3 | 88.0 | 74.0 | 97.3 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 55.0 | 87.0 | 72.3 | 96.0 | 14022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.7 | 25.0 | 56.3 | 56.7 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.9 | 28.0 | 51.9 | 52.5 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.7 | 28.0 | 56.4 | 57.0 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.8 | 30.0 | 60.2 | 60.6 | 14022 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 57.0 | 82.0 | 73.6 | 90.0 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 64.2 | 90.0 | 74.4 | 93.1 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.0 | 89.0 | 77.4 | 97.3 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 58.0 | 78.0 | 74.8 | 95.5 | 14022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.6 | 26.0 | 57.2 | 69.3 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.1 | 29.0 | 53.4 | 70.2 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.6 | 30.0 | 58.5 | 80.7 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 32.1 | 59.0 | 62.1 | 86.2 | 14022 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 65.9 | 83.0 | 79.1 | 91.2 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 63.4 | 85.0 | 78.8 | 92.8 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.4 | 89.0 | 83.1 | 97.0 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 58.6 | 81.0 | 81.9 | 96.2 | 14022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.3 | 26.0 | 56.4 | 60.4 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.0 | 29.0 | 52.3 | 60.5 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 28.4 | 95.0 | 57.4 | 72.0 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 32.2 | 82.0 | 60.6 | 70.5 | 14022 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 61.2 | 98.0 | 79.8 | 91.2 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 73.9 | 94.0 | 80.6 | 93.4 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 75.8 | 100.0 | 84.9 | 98.0 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 67.1 | 98.0 | 84.1 | 96.2 | 14022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.6 | 68.0 | 57.9 | 80.3 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 83.0 | 54.6 | 71.2 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.9 | 100.0 | 58.7 | 80.3 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 30.8 | 96.0 | 61.9 | 81.8 | 14022 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 59.4 | 100.0 | 81.7 | 101.6 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 65.8 | 100.0 | 84.0 | 105.6 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 67.3 | 100.0 | 87.2 | 107.2 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 64.9 | 100.0 | 86.8 | 106.2 | 14022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.8 | 61.0 | 60.4 | 97.2 | 11882 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.2 | 92.0 | 58.1 | 104.2 | 13388 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 30.8 | 87.0 | 61.8 | 106.9 | 13388 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 41.6 | 100.0 | 64.9 | 107.5 | 14022 |

