# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_145838/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 1 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 507.66 | 0.50 | 35.40 | 3.62 | 4.12 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 629.18 | 0.81 | 35.65 | 3.59 | 4.62 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 616.16 | 1.66 | 35.66 | 3.59 | 5.61 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 652.20 | 3.14 | 37.30 | 3.43 | 7.21 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 666.22 | 6.15 | 36.38 | 3.52 | 10.84 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 665.42 | 12.31 | 35.70 | 3.58 | 18.11 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 646.72 | 25.33 | 34.80 | 3.68 | 33.31 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 597.06 | 54.88 | 32.64 | 3.92 | 67.62 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 515.70 | 127.08 | 28.55 | 4.48 | 149.44 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 448.77 | 222.83 | 25.41 | 5.04 | 262.59 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 104.2 | 104.2 | 14854 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 120.7 | 120.7 | 21342 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 2.0 | 2.0 | 108.9 | 108.9 | 21342 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 1.0 | 1.0 | 110.7 | 110.7 | 21342 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 93.3 | 96.0 | 172.0 | 192.8 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 96.0 | 96.0 | 212.0 | 240.5 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 95.7 | 96.0 | 197.5 | 224.2 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 96.0 | 96.0 | 199.5 | 223.8 | 21398 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 153.9 | 153.9 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 186.2 | 186.2 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 161.0 | 161.0 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 162.6 | 162.6 | 21398 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 75.3 | 97.0 | 165.1 | 194.0 | 14984 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 74.7 | 97.0 | 200.4 | 243.2 | 21472 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 75.3 | 98.0 | 187.4 | 226.2 | 21472 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 73.3 | 97.0 | 188.5 | 224.7 | 21472 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 50.0 | 100.0 | 116.1 | 122.5 | 15022 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 134.8 | 143.1 | 21510 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 122.4 | 130.6 | 21510 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 131.3 | 145.0 | 21510 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 66.3 | 98.0 | 172.0 | 193.2 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 62.3 | 98.0 | 212.4 | 244.4 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 60.3 | 98.0 | 194.9 | 227.3 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 62.3 | 98.0 | 195.1 | 226.1 | 21562 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 66.7 | 100.0 | 147.4 | 180.2 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 178.0 | 224.3 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 58.3 | 100.0 | 163.1 | 207.2 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 58.3 | 100.0 | 166.6 | 208.5 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 97.8 | 100.0 | 174.0 | 194.7 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.8 | 100.0 | 218.7 | 249.2 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.8 | 100.0 | 199.5 | 226.4 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.8 | 100.0 | 200.6 | 226.8 | 21562 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 67.2 | 100.0 | 135.7 | 152.1 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 67.2 | 100.0 | 162.4 | 184.3 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.8 | 100.0 | 146.5 | 166.0 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 65.7 | 100.0 | 147.7 | 170.2 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 97.0 | 100.0 | 172.8 | 193.4 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.0 | 100.0 | 217.3 | 247.6 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.0 | 100.0 | 196.0 | 223.8 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.0 | 100.0 | 199.4 | 225.2 | 21562 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 69.9 | 100.0 | 140.7 | 152.9 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 67.8 | 100.0 | 170.8 | 185.8 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 71.9 | 100.0 | 152.1 | 166.8 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 70.9 | 100.0 | 156.1 | 170.9 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 93.4 | 100.0 | 167.0 | 193.6 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.8 | 100.0 | 209.0 | 248.2 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 93.6 | 100.0 | 188.3 | 224.5 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 91.0 | 100.0 | 191.0 | 225.5 | 21562 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 80.6 | 100.0 | 143.9 | 172.2 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.2 | 100.0 | 174.4 | 216.6 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.1 | 100.0 | 156.9 | 195.4 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 80.1 | 100.0 | 160.1 | 187.3 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 88.6 | 100.0 | 162.4 | 193.9 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 89.1 | 100.0 | 202.0 | 249.6 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.6 | 100.0 | 182.6 | 226.3 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.1 | 100.0 | 186.4 | 226.8 | 21562 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 81.5 | 100.0 | 142.3 | 154.1 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.4 | 100.0 | 173.1 | 192.8 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.1 | 100.0 | 156.6 | 175.1 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.7 | 100.0 | 159.6 | 177.1 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 99.5 | 100.0 | 159.4 | 192.8 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 99.2 | 100.0 | 201.9 | 247.9 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 99.4 | 100.0 | 183.5 | 227.0 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 99.4 | 100.0 | 185.4 | 227.1 | 21562 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.1 | 100.0 | 145.5 | 187.6 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.0 | 100.0 | 180.7 | 239.1 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.7 | 100.0 | 164.3 | 219.2 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.4 | 100.0 | 166.4 | 210.2 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 96.8 | 100.0 | 158.3 | 187.9 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 97.5 | 100.0 | 208.0 | 249.3 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 96.0 | 100.0 | 189.9 | 227.9 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 96.0 | 100.0 | 191.4 | 227.8 | 21562 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 80.8 | 100.0 | 142.6 | 156.5 | 15074 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.6 | 100.0 | 180.2 | 211.4 | 21562 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.4 | 100.0 | 165.2 | 194.4 | 21562 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.1 | 100.0 | 167.1 | 196.1 | 21562 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 93.1 | 100.0 | 156.6 | 185.8 | 15076 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.1 | 100.0 | 210.6 | 249.5 | 21564 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 95.9 | 100.0 | 194.2 | 228.1 | 21564 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 94.0 | 100.0 | 195.0 | 228.4 | 21564 |

