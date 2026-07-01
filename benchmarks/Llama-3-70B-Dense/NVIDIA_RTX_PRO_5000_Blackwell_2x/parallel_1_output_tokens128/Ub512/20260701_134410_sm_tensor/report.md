# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `103000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `512`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `1/1`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260701_134410/llama_server.log`

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
./build/bin/llama-server -m /workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 103000 --override-kv llama.context_length=int:103000 -b 16384 -ub 512 -np 1 -ctk f16 -sm tensor -ts 1/1
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 1074.45 | 0.24 | 38.63 | 3.31 | 3.56 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 1394.87 | 0.37 | 38.60 | 3.32 | 3.80 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 1177.77 | 0.87 | 38.07 | 3.36 | 4.43 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 1233.31 | 1.66 | 38.57 | 3.32 | 5.31 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 1308.03 | 3.13 | 37.64 | 3.40 | 7.13 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 1317.56 | 6.22 | 37.16 | 3.44 | 10.82 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 1287.15 | 12.73 | 35.69 | 3.59 | 18.34 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 1200.83 | 27.29 | 32.79 | 3.90 | 35.43 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 992.27 | 66.04 | 28.64 | 4.47 | 79.27 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 791.10 | 126.40 | 25.31 | 5.06 | 147.90 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 108.9 | 108.9 | 37150 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 21.0 | 21.0 | 92.4 | 92.4 | 37150 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.0 | 98.0 | 280.4 | 301.0 | 37194 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 97.5 | 98.0 | 280.8 | 300.5 | 37194 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 31.0 | 31.0 | 287.8 | 287.8 | 37194 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 277.0 | 277.0 | 37194 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 97.7 | 98.0 | 285.8 | 301.1 | 37250 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.0 | 98.0 | 287.5 | 300.3 | 37250 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 94.2 | 94.2 | 37250 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 90.1 | 90.1 | 37250 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 78.0 | 98.0 | 281.4 | 305.2 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 69.7 | 98.0 | 274.9 | 301.0 | 37292 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 41.5 | 83.0 | 232.4 | 232.7 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 14.5 | 29.0 | 218.6 | 227.6 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.0 | 98.0 | 287.6 | 301.8 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.0 | 98.0 | 288.2 | 301.1 | 37292 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 57.7 | 99.0 | 212.5 | 279.5 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 66.0 | 99.0 | 204.0 | 281.3 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.3 | 99.0 | 286.3 | 299.8 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.3 | 99.0 | 289.8 | 299.9 | 37292 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 61.8 | 99.0 | 222.6 | 286.2 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 67.3 | 99.0 | 222.4 | 290.4 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.2 | 99.0 | 289.9 | 300.4 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.2 | 99.0 | 291.6 | 300.1 | 37292 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 77.4 | 99.0 | 240.5 | 294.5 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 77.2 | 99.0 | 240.8 | 298.4 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 95.0 | 98.0 | 292.8 | 300.3 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.4 | 99.0 | 294.5 | 300.0 | 37292 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 79.3 | 99.0 | 253.9 | 301.3 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 79.0 | 99.0 | 254.1 | 301.9 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 97.1 | 99.0 | 296.2 | 300.5 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 96.4 | 99.0 | 296.1 | 300.5 | 37292 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 83.9 | 100.0 | 269.8 | 302.6 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 84.2 | 100.0 | 269.0 | 301.9 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.2 | 100.0 | 298.0 | 301.1 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.2 | 100.0 | 298.1 | 302.1 | 37292 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 83.7 | 100.0 | 269.1 | 303.7 | 37292 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 83.6 | 100.0 | 267.9 | 303.4 | 37292 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 98.6 | 100.0 | 299.1 | 302.6 | 37294 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 99.1 | 100.0 | 299.2 | 304.1 | 37294 |

