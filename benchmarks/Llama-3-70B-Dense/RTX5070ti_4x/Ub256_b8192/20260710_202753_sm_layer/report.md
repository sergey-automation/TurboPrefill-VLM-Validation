# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `256`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_202753/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 256 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 307.07 | 0.93 | 9.27 | 13.81 | 14.75 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 333.70 | 1.66 | 9.25 | 13.84 | 15.61 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 344.48 | 3.28 | 9.15 | 13.98 | 17.43 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 342.83 | 6.28 | 9.02 | 14.19 | 20.74 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 336.06 | 12.72 | 8.74 | 14.64 | 27.85 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 324.56 | 26.15 | 8.72 | 14.68 | 41.69 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 301.03 | 58.64 | 8.18 | 15.65 | 75.96 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 259.44 | 133.34 | 7.37 | 17.36 | 154.38 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 42.0 | 42.0 | 46.4 | 46.4 | 11988 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 38.0 | 38.0 | 13486 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 42.0 | 42.0 | 13486 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 44.1 | 44.1 | 14120 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.9 | 25.0 | 56.2 | 57.8 | 11988 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.5 | 28.0 | 52.2 | 53.4 | 13494 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.5 | 28.0 | 56.2 | 57.5 | 13494 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.1 | 30.0 | 60.1 | 61.3 | 14128 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 47.6 | 56.4 | 11988 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 40.0 | 80.0 | 43.4 | 55.5 | 13494 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 9.5 | 19.0 | 42.3 | 48.5 | 13494 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 1.5 | 3.0 | 42.9 | 48.5 | 14128 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.0 | 25.0 | 56.0 | 57.0 | 11988 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.1 | 28.0 | 51.9 | 53.6 | 13494 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.1 | 28.0 | 55.8 | 56.5 | 13494 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 28.1 | 30.0 | 60.7 | 63.4 | 14128 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 51.5 | 57.1 | 11988 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 45.1 | 50.2 | 13494 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 2.3 | 7.0 | 51.7 | 59.0 | 13494 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 29.7 | 89.0 | 50.4 | 52.2 | 14128 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.6 | 25.0 | 56.1 | 56.7 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.7 | 28.0 | 51.9 | 52.9 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 29.9 | 84.0 | 56.2 | 57.0 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 30.9 | 74.0 | 59.9 | 60.8 | 14130 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 7.7 | 46.0 | 53.6 | 59.0 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 17.5 | 60.0 | 48.5 | 55.7 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.3 | 100.0 | 53.0 | 59.7 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 16.7 | 100.0 | 52.1 | 57.8 | 14130 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.7 | 25.0 | 56.1 | 56.6 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.7 | 28.0 | 51.9 | 52.6 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.5 | 29.0 | 55.9 | 56.7 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 27.1 | 31.0 | 60.3 | 61.8 | 14130 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.2 | 100.0 | 50.7 | 56.4 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 6.8 | 45.0 | 46.6 | 54.7 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 34.8 | 100.0 | 49.9 | 58.9 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 15.4 | 100.0 | 51.3 | 60.3 | 14130 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.3 | 26.0 | 55.8 | 57.1 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.1 | 29.0 | 52.1 | 53.0 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.5 | 30.0 | 56.2 | 58.0 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.7 | 32.0 | 59.6 | 60.9 | 14130 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 13.3 | 100.0 | 51.8 | 57.4 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 34.2 | 100.0 | 47.0 | 57.2 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.8 | 100.0 | 51.7 | 60.6 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 22.0 | 100.0 | 51.9 | 60.9 | 14130 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.7 | 26.0 | 55.5 | 57.0 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.8 | 29.0 | 51.5 | 52.5 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.4 | 29.0 | 55.6 | 56.6 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 28.1 | 32.0 | 59.2 | 60.6 | 14130 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.8 | 100.0 | 52.6 | 60.5 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.1 | 100.0 | 47.5 | 56.5 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.7 | 100.0 | 51.6 | 61.2 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 23.3 | 100.0 | 52.4 | 61.8 | 14130 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.3 | 28.0 | 55.4 | 56.7 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 50.6 | 52.0 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.2 | 31.0 | 54.7 | 56.5 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 23.2 | 34.0 | 58.6 | 67.5 | 14130 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.8 | 100.0 | 54.1 | 60.9 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 29.9 | 100.0 | 49.0 | 57.1 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.7 | 100.0 | 52.7 | 61.3 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 20.6 | 100.0 | 53.8 | 61.2 | 14130 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.2 | 31.0 | 56.0 | 61.4 | 11990 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.8 | 100.0 | 51.0 | 55.0 | 13496 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.9 | 100.0 | 54.0 | 59.0 | 13496 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.3 | 36.0 | 57.8 | 67.6 | 14130 |

