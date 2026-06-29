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
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_123543/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 467.91 | 0.54 | 18.70 | 6.85 | 7.39 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 518.92 | 0.98 | 18.70 | 6.85 | 7.97 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 513.74 | 1.99 | 18.62 | 6.87 | 9.10 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 511.23 | 4.00 | 18.46 | 6.93 | 11.34 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 498.96 | 8.21 | 18.18 | 7.04 | 16.00 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 474.99 | 17.24 | 17.70 | 7.23 | 25.93 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 440.76 | 37.17 | 16.80 | 7.62 | 47.63 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 384.07 | 85.31 | 15.24 | 8.40 | 99.70 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 299.20 | 219.03 | 12.84 | 9.97 | 241.30 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 235.37 | 424.85 | 11.03 | 11.60 | 460.37 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 99.9 | 99.9 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 113.2 | 113.2 | 20554 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 108.9 | 108.9 | 20554 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.0 | 109.0 | 21010 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.5 | 24.0 | 139.9 | 142.8 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.7 | 27.0 | 160.6 | 162.5 | 20566 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.2 | 27.0 | 149.9 | 151.5 | 20566 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.8 | 29.0 | 156.3 | 159.1 | 21022 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 116.0 | 116.0 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 132.3 | 132.3 | 20566 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 118.8 | 118.8 | 20566 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 122.6 | 122.6 | 21022 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.0 | 24.0 | 139.6 | 143.0 | 19278 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.8 | 27.0 | 160.1 | 163.8 | 20574 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.2 | 27.0 | 148.5 | 151.7 | 20574 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.8 | 29.0 | 154.7 | 159.8 | 21030 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 6.0 | 12.0 | 149.3 | 157.5 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 56.5 | 100.0 | 165.0 | 169.0 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 122.8 | 146.9 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 7.5 | 15.0 | 129.0 | 157.4 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 21.3 | 24.0 | 134.8 | 143.3 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.8 | 27.0 | 154.4 | 163.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.2 | 27.0 | 155.1 | 171.7 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.3 | 29.0 | 159.5 | 170.7 | 21046 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 3.0 | 12.0 | 138.2 | 158.7 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.2 | 100.0 | 159.6 | 184.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.0 | 76.0 | 133.1 | 175.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.2 | 100.0 | 132.5 | 157.5 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.2 | 25.0 | 135.7 | 142.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.5 | 28.0 | 156.0 | 163.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.7 | 28.0 | 154.2 | 168.4 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.7 | 29.0 | 159.1 | 164.2 | 21046 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 13.0 | 100.0 | 131.2 | 159.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 151.6 | 189.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.6 | 95.0 | 135.0 | 177.1 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.4 | 100.0 | 131.0 | 161.4 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.3 | 25.0 | 135.9 | 142.9 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.5 | 28.0 | 157.2 | 165.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 28.0 | 153.3 | 160.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.0 | 30.0 | 159.2 | 165.6 | 21046 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 17.9 | 100.0 | 128.4 | 166.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.4 | 100.0 | 147.4 | 190.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.6 | 100.0 | 133.3 | 185.1 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.1 | 100.0 | 131.1 | 167.1 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.4 | 26.0 | 133.2 | 143.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.3 | 29.0 | 164.2 | 169.9 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.1 | 73.0 | 153.7 | 187.1 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.1 | 93.0 | 154.8 | 188.1 | 21046 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.4 | 100.0 | 128.3 | 172.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.8 | 100.0 | 152.0 | 204.7 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.0 | 100.0 | 136.5 | 186.4 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 13.0 | 100.0 | 132.7 | 183.5 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 26.0 | 100.0 | 135.7 | 156.2 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.7 | 100.0 | 158.3 | 198.9 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 17.3 | 30.0 | 149.1 | 190.5 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.9 | 100.0 | 151.7 | 167.9 | 21046 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.2 | 100.0 | 128.7 | 189.5 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.8 | 100.0 | 150.2 | 227.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.4 | 100.0 | 135.3 | 213.9 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.2 | 100.0 | 131.9 | 198.4 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.5 | 100.0 | 136.4 | 197.5 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.8 | 40.0 | 157.1 | 220.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.2 | 100.0 | 141.9 | 173.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.6 | 100.0 | 144.9 | 169.4 | 21046 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.4 | 100.0 | 129.2 | 234.2 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.0 | 100.0 | 151.6 | 249.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.8 | 100.0 | 130.9 | 247.4 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.8 | 100.0 | 132.2 | 245.5 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.7 | 100.0 | 131.1 | 217.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.1 | 100.0 | 152.8 | 249.3 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.7 | 100.0 | 142.0 | 242.8 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.3 | 100.0 | 143.0 | 211.9 | 21046 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.3 | 100.0 | 128.6 | 245.4 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.2 | 100.0 | 148.6 | 249.8 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 131.6 | 246.3 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.9 | 100.0 | 131.8 | 246.6 | 21046 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.7 | 100.0 | 126.4 | 244.0 | 19296 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.9 | 100.0 | 154.3 | 248.6 | 20592 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 100.0 | 140.6 | 243.6 | 20592 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.9 | 100.0 | 139.4 | 243.4 | 21048 |

