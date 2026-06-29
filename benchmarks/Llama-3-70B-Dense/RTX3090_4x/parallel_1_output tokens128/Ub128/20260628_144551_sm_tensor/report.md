# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `128`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_144551/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 1 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 455.09 | 0.56 | 35.42 | 3.61 | 4.18 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 386.40 | 1.32 | 35.96 | 3.56 | 5.10 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 397.18 | 2.57 | 36.42 | 3.51 | 6.45 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 442.54 | 4.62 | 34.63 | 3.70 | 8.96 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 456.68 | 8.96 | 35.74 | 3.58 | 13.72 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 451.84 | 18.13 | 36.08 | 3.55 | 23.89 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 477.93 | 34.28 | 33.07 | 3.87 | 42.43 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 460.47 | 71.16 | 32.51 | 3.94 | 83.90 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 414.65 | 158.05 | 27.52 | 4.65 | 180.51 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 374.11 | 267.29 | 24.51 | 5.22 | 307.29 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 1.0 | 1.0 | 95.4 | 95.4 | 14058 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 111.5 | 111.5 | 20546 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 101.7 | 101.7 | 20546 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.0 | 33.0 | 102.3 | 102.3 | 20546 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 72.3 | 96.0 | 167.9 | 190.4 | 14114 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 73.3 | 96.0 | 206.3 | 237.6 | 20602 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.0 | 96.0 | 196.1 | 223.7 | 20602 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 91.7 | 96.0 | 198.1 | 226.2 | 20602 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 35.0 | 70.0 | 136.1 | 152.6 | 14146 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.0 | 86.0 | 160.7 | 184.8 | 20634 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 153.6 | 172.7 | 20634 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 154.5 | 175.8 | 20634 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 98.0 | 98.0 | 173.8 | 192.3 | 14202 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 98.0 | 98.0 | 215.2 | 241.3 | 20690 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.7 | 98.0 | 202.2 | 227.4 | 20690 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 98.0 | 98.0 | 202.0 | 227.3 | 20690 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.7 | 83.0 | 129.4 | 136.8 | 14298 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 40.3 | 69.0 | 151.5 | 164.2 | 20786 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.7 | 77.0 | 141.2 | 152.2 | 20786 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.7 | 86.0 | 136.1 | 142.1 | 20786 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 78.0 | 98.0 | 169.0 | 192.3 | 14326 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.0 | 98.0 | 209.8 | 243.3 | 20814 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 92.3 | 98.0 | 199.1 | 227.6 | 20814 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.7 | 98.0 | 197.4 | 225.7 | 20814 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 39.2 | 98.0 | 133.4 | 153.0 | 14374 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.8 | 100.0 | 158.7 | 187.5 | 20862 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.2 | 98.0 | 147.3 | 173.8 | 20862 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.2 | 100.0 | 148.6 | 175.3 | 20862 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 82.5 | 98.0 | 156.2 | 193.3 | 14492 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 73.8 | 98.0 | 192.3 | 245.2 | 20980 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 72.5 | 98.0 | 180.0 | 228.2 | 20980 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 71.2 | 98.0 | 180.4 | 225.9 | 20980 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 58.0 | 100.0 | 134.5 | 178.3 | 14640 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 57.5 | 100.0 | 161.0 | 222.6 | 21128 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 62.8 | 100.0 | 146.4 | 194.7 | 21128 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.4 | 100.0 | 147.7 | 195.5 | 21128 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 71.2 | 96.0 | 163.7 | 190.5 | 14640 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.8 | 97.0 | 203.1 | 242.8 | 21128 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 68.0 | 96.0 | 184.8 | 222.9 | 21128 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.8 | 96.0 | 184.1 | 218.0 | 21128 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 66.6 | 100.0 | 136.2 | 186.2 | 14814 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.8 | 100.0 | 164.4 | 236.6 | 21302 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 72.3 | 100.0 | 148.0 | 215.9 | 21302 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 77.8 | 100.0 | 150.2 | 217.3 | 21302 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 76.4 | 100.0 | 155.0 | 193.5 | 14914 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 69.4 | 100.0 | 193.2 | 248.8 | 21402 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 69.6 | 100.0 | 176.4 | 225.4 | 21402 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 59.4 | 100.0 | 176.8 | 226.4 | 21402 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 75.5 | 100.0 | 137.1 | 179.8 | 14980 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 73.9 | 100.0 | 165.8 | 227.9 | 21468 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 74.3 | 100.0 | 149.8 | 195.1 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 71.1 | 100.0 | 151.7 | 198.0 | 21468 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 97.7 | 100.0 | 155.2 | 193.8 | 14980 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 98.0 | 100.0 | 193.6 | 248.7 | 21468 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.7 | 100.0 | 175.5 | 225.8 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 98.4 | 100.0 | 178.0 | 227.1 | 21468 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 79.7 | 100.0 | 138.3 | 180.3 | 14980 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.1 | 100.0 | 168.7 | 227.9 | 21468 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 78.6 | 100.0 | 153.0 | 205.3 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.0 | 100.0 | 155.3 | 210.3 | 21490 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 88.8 | 100.0 | 157.1 | 192.2 | 14980 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.1 | 100.0 | 200.4 | 249.5 | 21468 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.2 | 100.0 | 182.6 | 226.3 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.8 | 100.0 | 184.6 | 227.0 | 21490 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 79.1 | 100.0 | 140.6 | 153.4 | 14980 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 78.7 | 100.0 | 175.4 | 201.6 | 21478 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.8 | 100.0 | 160.0 | 183.9 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.2 | 100.0 | 161.8 | 184.6 | 21498 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 95.5 | 100.0 | 157.4 | 190.1 | 14980 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.0 | 100.0 | 206.6 | 248.2 | 21478 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.3 | 100.0 | 188.4 | 227.4 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 95.6 | 100.0 | 189.5 | 227.6 | 21498 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 80.4 | 100.0 | 141.7 | 155.8 | 14990 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.3 | 100.0 | 180.2 | 211.8 | 21478 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.4 | 100.0 | 164.8 | 193.2 | 21468 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.5 | 100.0 | 166.1 | 194.4 | 21498 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 93.2 | 100.0 | 156.0 | 186.1 | 14992 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.8 | 100.0 | 212.5 | 249.4 | 21480 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 95.2 | 100.0 | 194.6 | 228.0 | 21470 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 96.2 | 100.0 | 195.1 | 228.0 | 21500 |

