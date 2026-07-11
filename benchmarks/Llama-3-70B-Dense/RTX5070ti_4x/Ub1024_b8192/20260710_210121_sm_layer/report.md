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
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp-turboprefill-mtp/bench_reports_Llama3_70B/20260710_210121/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/Q4_K_M/Q4_K_M-00001-of-00001.gguf --host 0.0.0.0 --port 8081 -lv 4 -ngl 99 -c 35700 --override-kv llama.context_length=int:35700 -b 8192 -ub 1024 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 286 | 128 | 325.27 | 0.88 | 9.27 | 13.81 | 14.70 |
| ctx_000512.txt | 1 | 1 | 555 | 128 | 353.03 | 1.57 | 9.25 | 13.84 | 15.50 |
| ctx_001024.txt | 1 | 1 | 1131 | 128 | 358.24 | 3.16 | 9.16 | 13.97 | 17.29 |
| ctx_002048.txt | 1 | 1 | 2153 | 128 | 517.30 | 4.16 | 9.02 | 14.19 | 18.62 |
| ctx_004096.txt | 1 | 1 | 4273 | 128 | 690.26 | 6.19 | 8.74 | 14.64 | 21.37 |
| ctx_008192.txt | 1 | 1 | 8486 | 128 | 826.86 | 10.26 | 8.72 | 14.68 | 25.80 |
| ctx_016384.txt | 1 | 1 | 17651 | 128 | 706.39 | 24.99 | 8.18 | 15.64 | 42.25 |
| ctx_032768.txt | 1 | 1 | 34593 | 128 | 585.34 | 59.10 | 7.37 | 17.36 | 80.11 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 7.0 | 7.0 | 44.3 | 44.3 | 12620 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 37.7 | 37.7 | 14116 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 42.3 | 42.3 | 14116 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.0 | 0.0 | 43.5 | 43.5 | 14750 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.9 | 25.0 | 55.9 | 57.8 | 12620 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.4 | 28.0 | 52.0 | 53.5 | 14126 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.5 | 28.0 | 56.6 | 57.8 | 14126 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 27.1 | 30.0 | 59.7 | 61.4 | 14760 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 56.1 | 57.7 | 12628 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 2.0 | 4.0 | 51.5 | 53.5 | 14134 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 51.5 | 100.0 | 53.6 | 54.3 | 14134 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 0.5 | 1.0 | 47.8 | 58.5 | 14760 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.4 | 25.0 | 56.1 | 57.5 | 12628 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.1 | 28.0 | 51.7 | 52.2 | 14134 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.4 | 28.0 | 56.1 | 57.3 | 14134 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.7 | 30.0 | 61.1 | 70.0 | 14768 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 0.0 | 0.0 | 51.7 | 72.1 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 46.1 | 50.8 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 51.2 | 73.0 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 21.0 | 63.0 | 40.8 | 45.0 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 20.8 | 25.0 | 55.6 | 57.1 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.0 | 28.0 | 51.3 | 52.5 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.4 | 28.0 | 55.6 | 57.4 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.4 | 31.0 | 61.8 | 77.7 | 14782 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 31.2 | 100.0 | 58.3 | 78.0 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 51.9 | 87.2 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.5 | 100.0 | 59.9 | 75.9 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 25.0 | 100.0 | 55.1 | 88.6 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.2 | 25.0 | 55.8 | 56.7 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 26.0 | 28.0 | 51.8 | 52.8 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 24.8 | 29.0 | 56.1 | 57.0 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.5 | 30.0 | 60.9 | 68.7 | 14782 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 61.2 | 87.5 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 33.3 | 100.0 | 57.6 | 86.2 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 50.0 | 100.0 | 61.9 | 88.9 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 50.0 | 100.0 | 61.1 | 93.2 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.3 | 27.0 | 56.4 | 57.2 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 28.5 | 30.0 | 52.3 | 53.2 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.5 | 29.0 | 56.2 | 57.6 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 27.4 | 32.0 | 59.9 | 61.0 | 14782 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 53.5 | 100.0 | 66.8 | 89.9 | 12642 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 60.1 | 100.0 | 63.4 | 86.1 | 14148 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 56.0 | 100.0 | 67.5 | 91.9 | 14148 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 42.8 | 100.0 | 67.6 | 92.1 | 14782 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.9 | 26.0 | 55.4 | 57.0 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.6 | 29.0 | 52.0 | 53.1 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 23.6 | 29.0 | 56.1 | 57.2 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 26.3 | 32.0 | 60.0 | 61.0 | 14784 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 48.2 | 100.0 | 67.5 | 88.8 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 47.9 | 100.0 | 64.8 | 90.4 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 55.5 | 100.0 | 67.0 | 91.2 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 51.3 | 100.0 | 67.0 | 94.2 | 14784 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 18.7 | 28.0 | 54.4 | 56.9 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.3 | 31.0 | 50.1 | 52.7 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 27.7 | 100.0 | 56.5 | 79.5 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 30.2 | 100.0 | 60.4 | 68.8 | 14784 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 51.8 | 100.0 | 68.2 | 110.0 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 54.6 | 100.0 | 66.4 | 102.1 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 55.3 | 100.0 | 70.9 | 103.8 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 48.9 | 100.0 | 70.7 | 103.5 | 14784 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 21.8 | 100.0 | 55.3 | 72.2 | 12644 |
| 1 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 22.7 | 100.0 | 51.2 | 86.1 | 14150 |
| 2 | NVIDIA GeForce RTX 5070 Ti | Gen3 x8 | 25.5 | 100.0 | 55.1 | 92.4 | 14150 |
| 3 | NVIDIA GeForce RTX 5070 Ti | Gen3 x16 | 24.8 | 100.0 | 59.3 | 98.4 | 14784 |

