# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_125147/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 464.33 | 0.55 | 18.69 | 6.85 | 7.40 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 513.39 | 0.99 | 18.70 | 6.85 | 7.98 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 505.70 | 2.02 | 18.62 | 6.87 | 9.12 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 502.37 | 4.07 | 18.47 | 6.93 | 11.41 |
| ctx_004096.txt | 1 | 1 | 4094 | 96 | 695.14 | 5.89 | 18.23 | 5.27 | 11.92 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 875.40 | 9.36 | 17.72 | 7.23 | 18.03 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 958.37 | 17.09 | 16.81 | 7.62 | 27.56 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 799.86 | 40.97 | 15.25 | 8.40 | 55.36 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 572.04 | 114.56 | 12.84 | 9.97 | 136.89 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 429.53 | 232.81 | 11.03 | 11.61 | 268.29 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 102.4 | 102.4 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.6 | 116.6 | 20554 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.8 | 109.8 | 20554 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 111.6 | 111.6 | 21010 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.5 | 24.0 | 142.4 | 145.6 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.8 | 27.0 | 164.3 | 166.4 | 20566 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.7 | 27.0 | 151.3 | 153.0 | 20566 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.8 | 29.0 | 158.4 | 161.0 | 21022 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 118.6 | 118.6 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 135.5 | 135.5 | 20566 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 120.0 | 120.0 | 20566 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 129.1 | 129.1 | 21022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 17.5 | 24.0 | 141.8 | 146.0 | 19278 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.5 | 27.0 | 162.8 | 166.8 | 20574 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.0 | 27.0 | 150.2 | 153.8 | 20574 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.8 | 29.0 | 154.7 | 159.6 | 21030 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 6.0 | 12.0 | 151.4 | 159.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 56.5 | 100.0 | 173.6 | 184.0 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 123.2 | 146.7 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 126.7 | 151.5 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.0 | 25.0 | 137.8 | 146.4 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.5 | 27.0 | 159.0 | 168.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.8 | 27.0 | 155.2 | 171.9 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.8 | 29.0 | 160.4 | 168.6 | 21046 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 4.2 | 17.0 | 140.5 | 160.3 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 53.5 | 100.0 | 161.8 | 180.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.8 | 3.0 | 129.2 | 168.9 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 130.9 | 153.7 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.3 | 24.0 | 137.8 | 146.2 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.5 | 27.0 | 159.9 | 169.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.7 | 27.0 | 156.6 | 175.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.8 | 30.0 | 159.9 | 167.0 | 21046 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 49.8 | 100.0 | 134.8 | 201.9 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.0 | 100.0 | 165.5 | 232.7 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 34.3 | 100.0 | 137.5 | 210.0 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 6.3 | 38.0 | 131.1 | 214.6 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.8 | 25.0 | 137.3 | 145.3 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.4 | 28.0 | 157.7 | 166.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.8 | 28.0 | 152.9 | 157.4 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.4 | 30.0 | 159.3 | 162.5 | 21046 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.9 | 100.0 | 151.3 | 215.7 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.1 | 100.0 | 173.7 | 236.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.8 | 100.0 | 157.6 | 219.9 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 41.8 | 100.0 | 155.8 | 222.8 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.0 | 26.0 | 135.3 | 146.3 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.7 | 29.0 | 165.0 | 181.3 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.4 | 60.0 | 153.6 | 187.4 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.7 | 93.0 | 157.1 | 196.3 | 21046 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 42.9 | 100.0 | 159.7 | 209.3 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.5 | 100.0 | 188.5 | 236.7 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.9 | 100.0 | 169.2 | 221.5 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.9 | 100.0 | 161.5 | 214.3 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 14.8 | 27.0 | 136.1 | 177.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.4 | 100.0 | 156.5 | 166.3 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.1 | 36.0 | 146.5 | 190.1 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.1 | 100.0 | 156.4 | 198.4 | 21046 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 40.5 | 100.0 | 156.5 | 219.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.1 | 100.0 | 180.3 | 236.5 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 42.1 | 100.0 | 160.3 | 234.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.9 | 100.0 | 155.2 | 226.5 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 17.2 | 65.0 | 132.1 | 162.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.2 | 100.0 | 162.8 | 225.1 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 37.8 | 100.0 | 152.8 | 232.3 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.7 | 100.0 | 161.8 | 228.1 | 21046 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 44.6 | 100.0 | 151.0 | 228.9 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.7 | 100.0 | 174.2 | 230.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 40.4 | 100.0 | 158.6 | 244.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.4 | 100.0 | 154.9 | 236.3 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.6 | 100.0 | 136.8 | 239.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.7 | 100.0 | 163.3 | 249.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.5 | 100.0 | 154.6 | 230.3 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.2 | 100.0 | 161.6 | 233.8 | 21046 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 40.5 | 100.0 | 146.9 | 244.4 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.6 | 100.0 | 167.9 | 249.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.1 | 100.0 | 154.0 | 244.8 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.4 | 100.0 | 149.5 | 248.7 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.6 | 100.0 | 132.5 | 244.2 | 19296 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.8 | 100.0 | 158.7 | 248.8 | 20592 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.6 | 100.0 | 152.9 | 243.3 | 20592 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.3 | 100.0 | 158.0 | 242.6 | 21048 |

