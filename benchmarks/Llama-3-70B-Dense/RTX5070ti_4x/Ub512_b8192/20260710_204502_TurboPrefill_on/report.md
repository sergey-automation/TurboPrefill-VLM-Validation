# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `512`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_204502/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 512 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 323.61 | 0.88 | 9.27 | 13.81 | 14.70 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 345.92 | 1.60 | 9.25 | 13.84 | 15.54 |
| ctx_001024.txt | 1 | 1 | 1131 | 7 | 503.23 | 2.25 | 10.53 | 0.66 | 3.09 |
| ctx_002048.txt | 1 | 1 | 2153 | 2 | 694.85 | 3.10 | 17.49 | 0.11 | 3.45 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 847.82 | 5.04 | 8.74 | 14.65 | 20.15 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 932.79 | 9.10 | 8.73 | 14.67 | 24.64 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 833.01 | 21.19 | 8.18 | 15.64 | 38.50 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 714.35 | 48.43 | 7.38 | 17.35 | 69.45 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 1.0 | 1.0 | 44.1 | 44.1 | 12200 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 38.0 | 38.0 | 13696 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 41.8 | 41.8 | 13696 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 43.3 | 43.3 | 14330 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.5 | 25.0 | 56.1 | 57.0 | 12200 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.7 | 28.0 | 52.0 | 53.7 | 13706 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.4 | 28.0 | 56.2 | 57.7 | 13706 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.8 | 30.0 | 59.6 | 61.3 | 14340 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 54.2 | 55.7 | 12206 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 49.6 | 51.3 | 13712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 54.0 | 55.6 | 13712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 48.0 | 55.4 | 14346 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.6 | 25.0 | 56.2 | 57.5 | 12206 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.3 | 28.0 | 51.4 | 52.3 | 13712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.3 | 28.0 | 56.1 | 57.6 | 13712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.1 | 30.0 | 61.4 | 67.9 | 14346 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 57.6 | 72.7 | 12206 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 50.4 | 65.1 | 13712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 45.3 | 50.0 | 13712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 40.7 | 44.1 | 14346 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 43.6 | 43.6 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 39.0 | 39.0 | 43.4 | 43.4 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 60.0 | 60.0 | 62.3 | 62.3 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 78.8 | 78.8 | 14348 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 67.9 | 82.0 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 65.0 | 100.0 | 65.3 | 86.5 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 66.7 | 100.0 | 61.6 | 89.0 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 22.3 | 67.0 | 57.3 | 82.3 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 53.4 | 100.0 | 64.9 | 85.1 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 53.0 | 100.0 | 62.0 | 85.5 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 43.4 | 100.0 | 67.0 | 87.8 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 53.6 | 100.0 | 64.4 | 89.3 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.8 | 26.0 | 55.9 | 57.0 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.8 | 29.0 | 51.7 | 53.3 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.5 | 29.0 | 55.5 | 57.3 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.3 | 31.0 | 60.3 | 64.7 | 14348 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 60.6 | 100.0 | 71.3 | 87.1 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 51.9 | 100.0 | 70.9 | 85.9 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 67.4 | 100.0 | 73.7 | 89.9 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 61.0 | 100.0 | 70.4 | 89.2 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.8 | 26.0 | 55.0 | 56.7 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 29.7 | 100.0 | 50.4 | 52.9 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.8 | 29.0 | 55.1 | 60.1 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.6 | 32.0 | 60.1 | 63.5 | 14348 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 54.5 | 100.0 | 71.3 | 92.2 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 67.6 | 100.0 | 69.8 | 86.9 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 73.5 | 100.0 | 72.5 | 91.2 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 49.8 | 100.0 | 71.5 | 90.0 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.1 | 28.0 | 54.7 | 56.1 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.5 | 31.0 | 51.3 | 52.6 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.0 | 32.0 | 56.9 | 74.7 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 31.3 | 100.0 | 61.1 | 92.2 | 14348 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 63.8 | 100.0 | 74.9 | 104.1 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 64.7 | 100.0 | 72.6 | 105.7 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 59.6 | 100.0 | 75.5 | 104.5 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 52.8 | 100.0 | 74.4 | 105.0 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.4 | 93.0 | 53.9 | 58.6 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.1 | 35.0 | 52.9 | 82.6 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 32.6 | 100.0 | 59.3 | 105.4 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 22.2 | 100.0 | 63.4 | 102.6 | 14348 |

