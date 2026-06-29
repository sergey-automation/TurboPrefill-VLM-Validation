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
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_120544/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
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
| ctx_000256.txt | 1 | 1 | 254 | 128 | 445.79 | 0.57 | 18.69 | 6.85 | 7.42 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 678.04 | 0.75 | 18.69 | 6.85 | 7.74 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 942.77 | 1.08 | 18.61 | 6.88 | 8.19 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 1119.00 | 1.83 | 18.47 | 6.93 | 9.16 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 1218.95 | 3.36 | 18.18 | 7.04 | 11.15 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 1244.39 | 6.58 | 17.71 | 7.23 | 15.25 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 1208.06 | 13.56 | 16.80 | 7.62 | 24.02 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 957.86 | 34.21 | 15.24 | 8.40 | 48.60 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 659.29 | 99.40 | 12.84 | 9.97 | 121.65 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 485.58 | 205.93 | 11.03 | 11.60 | 241.33 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 99.2 | 99.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.3 | 116.3 | 19330 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.7 | 109.7 | 19330 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.6 | 109.6 | 19698 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.8 | 24.0 | 139.2 | 142.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.5 | 27.0 | 159.0 | 161.2 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.8 | 27.0 | 149.5 | 151.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.5 | 29.0 | 155.4 | 158.0 | 19706 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 117.5 | 117.5 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 133.8 | 133.8 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 121.1 | 121.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 127.9 | 127.9 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.2 | 24.0 | 141.3 | 142.8 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.2 | 27.0 | 160.9 | 162.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.5 | 27.0 | 150.6 | 153.2 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.3 | 29.0 | 156.9 | 159.7 | 19706 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 129.2 | 129.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 147.6 | 147.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 134.1 | 134.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 144.7 | 144.7 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 28.7 | 62.0 | 143.4 | 158.3 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.9 | 38.0 | 163.7 | 178.9 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 27.0 | 153.9 | 173.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.4 | 29.0 | 159.9 | 163.4 | 19706 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 30.5 | 61.0 | 131.3 | 160.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 42.0 | 84.0 | 148.7 | 179.9 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 41.5 | 83.0 | 133.5 | 158.0 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.5 | 77.0 | 131.1 | 152.8 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.3 | 24.0 | 144.0 | 154.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.2 | 28.0 | 165.8 | 186.8 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.3 | 27.0 | 156.4 | 180.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.2 | 29.0 | 162.3 | 185.5 | 19706 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 48.3 | 73.0 | 138.9 | 195.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.0 | 83.0 | 159.1 | 229.1 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 81.0 | 148.5 | 220.4 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.3 | 76.0 | 144.3 | 209.7 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.7 | 67.0 | 147.3 | 196.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.0 | 71.0 | 171.0 | 227.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.9 | 80.0 | 160.6 | 219.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.3 | 73.0 | 164.8 | 205.8 | 19706 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 48.3 | 74.0 | 161.1 | 196.3 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 53.2 | 84.0 | 188.4 | 232.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.2 | 83.0 | 170.2 | 220.5 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 44.3 | 73.0 | 166.9 | 211.7 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.1 | 70.0 | 147.1 | 192.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.9 | 80.0 | 173.4 | 227.0 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 34.2 | 77.0 | 162.6 | 214.7 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.5 | 75.0 | 165.3 | 204.2 | 19706 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 45.7 | 74.0 | 160.4 | 198.5 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.1 | 83.0 | 188.5 | 235.2 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.0 | 87.0 | 175.9 | 220.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.2 | 78.0 | 169.1 | 211.0 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.9 | 64.0 | 150.2 | 185.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 31.1 | 73.0 | 178.1 | 221.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.7 | 70.0 | 164.9 | 205.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.2 | 65.0 | 167.3 | 199.5 | 19706 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 43.9 | 85.0 | 158.4 | 205.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 51.4 | 93.0 | 186.5 | 242.2 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.9 | 91.0 | 171.1 | 224.7 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.8 | 91.0 | 167.3 | 217.2 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 42.8 | 100.0 | 153.4 | 181.6 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.8 | 82.0 | 179.0 | 213.8 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 41.2 | 90.0 | 164.2 | 196.7 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.8 | 86.0 | 166.8 | 191.6 | 19706 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 45.7 | 100.0 | 157.6 | 206.8 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 51.6 | 100.0 | 183.2 | 242.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 49.9 | 100.0 | 169.1 | 226.3 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.0 | 100.0 | 165.7 | 216.9 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 37.7 | 96.0 | 156.6 | 182.9 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 42.2 | 100.0 | 181.6 | 211.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.0 | 100.0 | 167.6 | 197.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 37.3 | 100.0 | 168.1 | 192.0 | 19706 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 44.0 | 100.0 | 153.6 | 205.4 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.6 | 100.0 | 177.0 | 238.8 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.5 | 100.0 | 163.4 | 224.8 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.1 | 100.0 | 160.8 | 217.0 | 19706 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 42.2 | 100.0 | 157.9 | 190.8 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.8 | 100.0 | 182.8 | 217.9 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.1 | 100.0 | 169.1 | 208.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.3 | 100.0 | 169.2 | 209.2 | 19706 |

