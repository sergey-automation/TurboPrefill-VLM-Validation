# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `103000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `512`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `1/1`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260701_125411/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
```

### nvidia_smi

```text
0, NVIDIA RTX PRO 5000 Blackwell, 580.105.08, 48935 MiB
1, NVIDIA RTX PRO 5000 Blackwell, 580.105.08, 48935 MiB
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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 103000 --override-kv llama.context_length=int:103000 -b 16384 -ub 512 -np 1 -ctk f16 -sm layer -ts 1/1
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 970.47 | 0.26 | 26.39 | 4.85 | 5.12 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 1060.62 | 0.48 | 26.25 | 4.88 | 5.45 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 1058.01 | 0.97 | 26.16 | 4.89 | 5.99 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 1049.64 | 1.95 | 25.82 | 4.96 | 7.16 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 1028.84 | 3.98 | 25.24 | 5.07 | 9.49 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 988.38 | 8.29 | 24.83 | 5.15 | 14.23 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 922.87 | 17.75 | 23.63 | 5.42 | 24.64 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 808.31 | 40.54 | 21.38 | 5.99 | 49.68 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 625.96 | 104.69 | 17.95 | 7.13 | 118.35 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 477.21 | 209.55 | 15.34 | 8.34 | 236.87 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 44.0 | 44.0 | 103.3 | 103.3 | 38158 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 84.2 | 84.2 | 36784 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 52.0 | 57.0 | 227.5 | 228.5 | 38158 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 50.8 | 56.0 | 230.2 | 232.2 | 36798 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 129.1 | 129.1 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 4.0 | 4.0 | 123.4 | 123.4 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 48.2 | 57.0 | 222.6 | 230.7 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 47.5 | 55.0 | 233.2 | 241.3 | 36806 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 162.7 | 162.7 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 158.7 | 158.7 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 48.5 | 56.0 | 226.6 | 233.6 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 50.0 | 57.0 | 227.7 | 231.6 | 36806 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 4.5 | 9.0 | 157.5 | 207.2 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 26.0 | 52.0 | 142.3 | 198.2 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 53.0 | 58.0 | 224.8 | 234.5 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 49.0 | 57.0 | 233.7 | 236.2 | 36806 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 45.2 | 100.0 | 178.1 | 220.1 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 29.0 | 85.0 | 162.1 | 201.6 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 54.8 | 59.0 | 224.7 | 236.3 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 44.2 | 48.0 | 231.3 | 234.0 | 36806 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 43.6 | 100.0 | 184.7 | 228.0 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 34.3 | 100.0 | 177.0 | 217.1 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 50.8 | 58.0 | 228.1 | 233.3 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 54.0 | 87.0 | 224.0 | 234.0 | 36806 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 40.1 | 100.0 | 199.1 | 235.8 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 51.9 | 100.0 | 183.0 | 213.4 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 67.2 | 100.0 | 227.3 | 235.7 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 49.2 | 100.0 | 219.9 | 238.6 | 36806 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 48.5 | 100.0 | 208.4 | 241.6 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 47.8 | 100.0 | 192.6 | 230.9 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 43.4 | 100.0 | 218.6 | 233.1 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 54.6 | 100.0 | 224.7 | 235.6 | 36806 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 44.6 | 100.0 | 200.5 | 243.6 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 49.7 | 100.0 | 192.8 | 231.5 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 25.2 | 56.0 | 223.1 | 229.5 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 74.8 | 100.0 | 208.3 | 242.6 | 36806 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 46.9 | 100.0 | 194.1 | 277.8 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 43.9 | 100.0 | 185.4 | 278.4 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 50.3 | 100.0 | 210.7 | 294.3 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 47.7 | 100.0 | 197.8 | 284.3 | 36806 |

