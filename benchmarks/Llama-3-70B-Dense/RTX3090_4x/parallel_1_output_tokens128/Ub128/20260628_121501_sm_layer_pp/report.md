# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `128`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_121501/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
```

### nvidia_smi

```text
0, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
1, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
2, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
3, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 444.39 | 0.57 | 18.69 | 6.85 | 7.42 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 476.04 | 1.07 | 18.68 | 6.85 | 8.07 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 474.82 | 2.15 | 18.61 | 6.88 | 9.26 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 469.59 | 4.36 | 18.47 | 6.93 | 11.70 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 457.58 | 8.95 | 18.18 | 7.04 | 16.74 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 435.63 | 18.80 | 17.71 | 7.23 | 27.48 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 399.94 | 40.96 | 16.81 | 7.62 | 51.43 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 341.30 | 96.01 | 15.24 | 8.40 | 110.39 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 263.24 | 248.95 | 12.84 | 9.97 | 271.24 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 212.43 | 470.74 | 11.03 | 11.61 | 506.17 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 111.2 | 111.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 119.6 | 119.6 | 19330 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 110.1 | 110.1 | 19330 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 111.1 | 111.1 | 19698 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.2 | 24.0 | 142.4 | 145.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.2 | 27.0 | 161.8 | 164.5 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.2 | 27.0 | 150.4 | 152.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.5 | 29.0 | 157.3 | 160.5 | 19706 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 120.4 | 120.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 136.2 | 136.2 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 122.1 | 122.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 123.5 | 123.5 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 18.8 | 24.0 | 141.4 | 145.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.2 | 27.0 | 160.9 | 165.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.5 | 70.0 | 149.5 | 153.0 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.2 | 66.0 | 155.0 | 160.4 | 19706 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 9.0 | 18.0 | 114.6 | 124.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.5 | 67.0 | 130.7 | 142.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.1 | 122.7 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.7 | 123.6 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.1 | 24.0 | 142.3 | 145.7 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.0 | 45.0 | 162.5 | 166.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.7 | 56.0 | 150.1 | 153.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.0 | 29.0 | 156.6 | 161.2 | 19706 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.2 | 49.0 | 122.1 | 132.7 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 8.5 | 25.0 | 139.3 | 150.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 12.0 | 36.0 | 127.1 | 137.8 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 14.5 | 26.0 | 127.7 | 138.4 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.1 | 44.0 | 141.2 | 144.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.6 | 27.0 | 162.9 | 167.5 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.4 | 27.0 | 150.5 | 153.8 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.3 | 29.0 | 157.0 | 163.0 | 19706 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 18.5 | 60.0 | 124.9 | 130.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 7.1 | 44.0 | 144.3 | 152.5 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 14.2 | 59.0 | 132.1 | 140.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.9 | 54.0 | 133.0 | 141.2 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 17.4 | 25.0 | 140.1 | 144.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.9 | 28.0 | 164.3 | 168.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.9 | 28.0 | 149.7 | 152.5 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.9 | 69.0 | 154.0 | 158.3 | 19706 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.9 | 66.0 | 127.5 | 137.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.3 | 77.0 | 149.4 | 155.5 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.8 | 74.0 | 134.0 | 141.4 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 8.1 | 55.0 | 134.4 | 140.6 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 26.9 | 53.0 | 140.1 | 145.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.3 | 28.0 | 161.6 | 168.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.3 | 29.0 | 148.6 | 153.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.4 | 31.0 | 153.4 | 159.3 | 19706 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.2 | 74.0 | 126.1 | 133.9 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.6 | 91.0 | 145.6 | 155.9 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 89.0 | 133.5 | 142.4 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.7 | 86.0 | 132.0 | 141.1 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 34.6 | 76.0 | 137.9 | 145.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.7 | 30.0 | 157.7 | 164.9 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 17.9 | 30.0 | 145.7 | 153.5 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 18.3 | 32.0 | 148.7 | 157.5 | 19706 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.4 | 88.0 | 126.7 | 136.6 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.4 | 98.0 | 144.6 | 155.1 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 18.5 | 98.0 | 133.1 | 143.8 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.2 | 99.0 | 131.4 | 141.7 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.0 | 78.0 | 135.6 | 144.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.8 | 33.0 | 154.2 | 164.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.8 | 94.0 | 144.5 | 151.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.5 | 97.0 | 145.8 | 156.1 | 19706 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.8 | 100.0 | 126.8 | 136.3 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.0 | 100.0 | 145.6 | 157.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.7 | 100.0 | 133.3 | 148.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.1 | 100.0 | 132.4 | 143.3 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 29.1 | 100.0 | 133.9 | 141.5 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.6 | 100.0 | 154.2 | 163.3 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.2 | 59.0 | 142.1 | 151.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.1 | 100.0 | 142.8 | 152.9 | 19706 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.7 | 100.0 | 126.7 | 147.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.4 | 100.0 | 145.2 | 166.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.2 | 100.0 | 133.3 | 155.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.2 | 100.0 | 132.2 | 152.9 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.1 | 100.0 | 132.2 | 145.6 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.6 | 100.0 | 151.7 | 163.8 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.9 | 100.0 | 140.1 | 153.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.5 | 100.0 | 139.5 | 151.2 | 19706 |

