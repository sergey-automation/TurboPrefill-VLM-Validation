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
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_204834/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 512 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 325.73 | 0.88 | 9.25 | 13.83 | 14.72 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 345.58 | 1.61 | 9.25 | 13.83 | 15.54 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 357.58 | 3.16 | 9.16 | 13.97 | 17.29 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 356.53 | 6.04 | 9.02 | 14.19 | 20.51 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 349.36 | 12.23 | 8.75 | 14.64 | 27.33 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 336.90 | 25.19 | 8.72 | 14.67 | 40.73 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 312.44 | 56.49 | 8.18 | 15.64 | 73.77 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 271.75 | 127.30 | 7.37 | 17.36 | 148.30 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 3.0 | 3.0 | 44.3 | 44.3 | 12200 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 37.9 | 37.9 | 13696 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 42.4 | 42.4 | 13696 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 44.0 | 44.0 | 14330 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.1 | 25.0 | 56.1 | 57.2 | 12200 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.1 | 28.0 | 52.5 | 53.4 | 13706 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.9 | 27.0 | 56.0 | 57.2 | 13706 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 28.3 | 30.0 | 59.9 | 61.6 | 14340 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 54.3 | 55.9 | 12206 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 50.8 | 53.6 | 13712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 52.7 | 53.0 | 13712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.5 | 46.0 | 47.6 | 55.5 | 14346 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.6 | 24.0 | 56.1 | 57.5 | 12206 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.1 | 28.0 | 51.7 | 52.3 | 13712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.3 | 28.0 | 55.9 | 57.5 | 13712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.2 | 30.0 | 61.3 | 68.9 | 14346 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 53.0 | 57.7 | 12206 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 47.3 | 51.2 | 13712 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 45.6 | 53.4 | 13712 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 44.5 | 50.5 | 14346 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.5 | 25.0 | 55.7 | 57.0 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.6 | 28.0 | 51.0 | 52.3 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.2 | 28.0 | 55.9 | 56.8 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.5 | 31.0 | 60.8 | 64.3 | 14348 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 16.7 | 100.0 | 50.6 | 56.2 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 32.8 | 100.0 | 44.0 | 53.1 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 48.0 | 56.3 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 16.7 | 100.0 | 50.4 | 58.3 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.3 | 25.0 | 56.3 | 56.8 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.2 | 28.0 | 52.1 | 52.6 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.6 | 28.0 | 56.1 | 58.0 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.7 | 31.0 | 59.8 | 60.5 | 14348 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 18.2 | 100.0 | 52.5 | 58.4 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.4 | 100.0 | 47.9 | 54.9 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 29.2 | 100.0 | 52.4 | 59.2 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.8 | 100.0 | 52.0 | 60.5 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.5 | 26.0 | 56.0 | 57.2 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.8 | 30.0 | 51.4 | 53.0 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.7 | 29.0 | 55.4 | 57.4 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 29.1 | 32.0 | 60.4 | 61.2 | 14348 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.8 | 100.0 | 52.1 | 60.8 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.3 | 100.0 | 46.8 | 56.0 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.6 | 100.0 | 51.1 | 61.5 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 31.5 | 100.0 | 52.4 | 61.3 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.8 | 26.0 | 55.7 | 57.0 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.7 | 29.0 | 51.3 | 52.7 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.5 | 29.0 | 55.5 | 56.8 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 33.3 | 88.0 | 59.4 | 60.7 | 14348 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.6 | 100.0 | 52.4 | 64.9 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.6 | 100.0 | 47.1 | 59.6 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.6 | 100.0 | 51.2 | 66.4 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.2 | 100.0 | 51.8 | 66.9 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.2 | 28.0 | 54.4 | 56.6 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.7 | 32.0 | 51.6 | 62.9 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 34.5 | 100.0 | 55.1 | 64.4 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 23.8 | 33.0 | 58.4 | 67.2 | 14348 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.1 | 100.0 | 53.3 | 75.3 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.2 | 100.0 | 48.8 | 76.6 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.2 | 100.0 | 53.0 | 78.5 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 22.1 | 100.0 | 53.2 | 80.2 | 14348 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.5 | 31.0 | 56.2 | 79.6 | 12208 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 29.2 | 100.0 | 50.7 | 54.4 | 13714 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 18.7 | 35.0 | 55.2 | 82.8 | 13714 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.7 | 81.0 | 58.5 | 68.8 | 14348 |

