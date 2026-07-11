# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf`
- NGL: `99`
- CTX_SIZE: `35700`
- N_GEN: `128`
- BATCH: `8192`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_205456/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 1024 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 326.03 | 0.88 | 9.27 | 13.81 | 14.70 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 352.75 | 1.57 | 9.25 | 13.84 | 15.51 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 358.15 | 3.16 | 9.16 | 13.97 | 17.29 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 357.05 | 6.03 | 9.02 | 14.19 | 20.48 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 349.99 | 12.21 | 8.74 | 14.64 | 27.32 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 337.45 | 25.15 | 8.72 | 14.68 | 40.71 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 312.37 | 56.51 | 8.18 | 15.64 | 73.78 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 266.01 | 130.05 | 7.37 | 17.36 | 151.09 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 2.0 | 2.0 | 44.3 | 44.3 | 12620 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 37.4 | 37.4 | 14116 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 42.7 | 42.7 | 14116 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 43.7 | 43.7 | 14750 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.9 | 25.0 | 56.5 | 57.7 | 12620 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.8 | 28.0 | 52.0 | 52.8 | 14126 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.2 | 28.0 | 56.3 | 57.3 | 14126 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 27.2 | 30.0 | 59.9 | 61.5 | 14760 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 57.2 | 59.9 | 12628 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 51.5 | 55.4 | 14134 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 51.5 | 100.0 | 52.6 | 52.9 | 14134 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 1.0 | 2.0 | 47.2 | 57.1 | 14760 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 17.7 | 24.0 | 56.2 | 57.2 | 12628 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.5 | 28.0 | 51.2 | 52.1 | 14134 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.3 | 28.0 | 56.6 | 57.5 | 14134 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.5 | 29.0 | 60.8 | 69.8 | 14768 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 50.6 | 72.5 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 44.1 | 54.1 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 12.0 | 28.0 | 50.4 | 78.3 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 23.0 | 66.0 | 38.4 | 40.7 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.2 | 25.0 | 56.4 | 57.5 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.3 | 28.0 | 50.9 | 52.1 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.9 | 29.0 | 55.6 | 56.9 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 23.8 | 30.0 | 61.4 | 76.1 | 14782 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 16.7 | 100.0 | 50.4 | 75.9 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.7 | 100.0 | 44.3 | 74.6 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.2 | 100.0 | 49.2 | 71.0 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 16.7 | 100.0 | 48.0 | 74.2 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.4 | 25.0 | 56.6 | 57.1 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.6 | 28.0 | 52.0 | 52.5 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.0 | 29.0 | 56.5 | 56.9 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.7 | 31.0 | 60.0 | 60.5 | 14782 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.8 | 100.0 | 52.2 | 77.7 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 18.5 | 100.0 | 45.2 | 71.8 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.8 | 100.0 | 51.0 | 80.8 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 13.6 | 100.0 | 48.0 | 79.7 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 16.8 | 26.0 | 55.7 | 57.7 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.8 | 29.0 | 51.1 | 52.9 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 31.2 | 73.0 | 54.9 | 57.1 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 22.2 | 31.0 | 61.6 | 76.7 | 14782 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.3 | 100.0 | 50.9 | 81.8 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.7 | 100.0 | 46.1 | 77.0 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.3 | 100.0 | 49.9 | 81.9 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.4 | 100.0 | 51.0 | 80.5 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 18.9 | 26.0 | 56.4 | 57.5 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.8 | 29.0 | 51.5 | 52.8 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.1 | 30.0 | 55.3 | 56.5 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 32.8 | 100.0 | 59.0 | 60.7 | 14784 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.7 | 100.0 | 52.3 | 87.7 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 28.7 | 100.0 | 47.5 | 90.1 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.1 | 100.0 | 50.9 | 92.3 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 22.2 | 100.0 | 51.1 | 95.0 | 14784 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.3 | 28.0 | 54.5 | 57.3 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 28.5 | 100.0 | 49.6 | 52.5 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 19.8 | 31.0 | 56.6 | 82.8 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 30.4 | 100.0 | 60.0 | 76.0 | 14784 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.7 | 100.0 | 53.9 | 108.9 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.2 | 100.0 | 48.2 | 106.1 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.0 | 100.0 | 52.8 | 108.9 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 23.8 | 100.0 | 52.9 | 112.6 | 14784 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.4 | 100.0 | 55.4 | 67.3 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.6 | 100.0 | 50.4 | 78.2 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.6 | 100.0 | 55.5 | 96.9 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 27.5 | 100.0 | 59.8 | 101.4 | 14784 |

