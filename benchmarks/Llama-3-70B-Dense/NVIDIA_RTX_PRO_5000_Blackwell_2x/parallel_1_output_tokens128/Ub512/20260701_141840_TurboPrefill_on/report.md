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
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260701_141840/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
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
| ctx_000256.txt | 1 | 1 | 254 | 128 | 944.25 | 0.27 | 26.25 | 4.88 | 5.15 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 1031.10 | 0.49 | 26.20 | 4.89 | 5.47 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 1062.04 | 0.96 | 26.15 | 4.90 | 5.99 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 1276.61 | 1.60 | 25.82 | 4.96 | 6.83 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 1481.44 | 2.76 | 25.24 | 5.07 | 8.26 |
| ctx_008192.txt | 1 | 1 | 8190 | 128 | 1524.94 | 5.37 | 24.84 | 5.15 | 11.62 |
| ctx_016384.txt | 1 | 1 | 16382 | 128 | 1572.07 | 10.42 | 23.65 | 5.41 | 17.30 |
| ctx_032768.txt | 1 | 1 | 32767 | 128 | 1301.71 | 25.17 | 21.40 | 5.98 | 34.32 |
| ctx_065536.txt | 1 | 1 | 65534 | 128 | 950.84 | 68.92 | 17.97 | 7.12 | 82.62 |
| ctx_100000.txt | 1 | 1 | 99998 | 128 | 708.50 | 141.14 | 15.36 | 8.33 | 163.45 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 63.0 | 63.0 | 103.9 | 103.9 | 38158 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 7.0 | 7.0 | 81.4 | 81.4 | 36798 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 48.0 | 55.0 | 220.2 | 225.3 | 38158 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 51.2 | 54.0 | 225.3 | 227.8 | 36798 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 99.1 | 99.1 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 4.0 | 4.0 | 90.2 | 90.2 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 53.2 | 56.0 | 222.0 | 226.0 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 49.8 | 56.0 | 232.0 | 244.3 | 36806 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.0 | 0.0 | 161.0 | 161.0 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 5.0 | 5.0 | 145.0 | 145.0 | 36806 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 53.5 | 57.0 | 221.0 | 230.7 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 51.2 | 57.0 | 230.2 | 231.5 | 36806 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 0.5 | 1.0 | 161.7 | 212.9 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 50.0 | 100.0 | 168.6 | 237.0 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 52.0 | 58.0 | 226.7 | 233.2 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 46.2 | 53.0 | 230.1 | 232.4 | 36808 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 36.0 | 100.0 | 236.6 | 286.0 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 54.0 | 100.0 | 224.5 | 297.8 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 54.5 | 59.0 | 229.8 | 234.0 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 54.5 | 58.0 | 230.8 | 233.1 | 36808 |

### ctx_008192.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 53.2 | 100.0 | 235.4 | 296.0 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 48.0 | 100.0 | 227.0 | 295.2 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 38.6 | 59.0 | 224.7 | 235.7 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 40.8 | 56.0 | 244.8 | 275.4 | 36808 |

### ctx_016384.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 76.2 | 100.0 | 247.4 | 303.1 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 51.9 | 100.0 | 235.5 | 298.8 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 52.3 | 100.0 | 235.9 | 301.4 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 62.8 | 100.0 | 241.6 | 292.7 | 36808 |

### ctx_032768.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 62.4 | 100.0 | 237.9 | 300.5 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 63.4 | 100.0 | 231.6 | 304.3 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 38.4 | 60.0 | 238.3 | 284.3 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 67.9 | 100.0 | 237.8 | 284.9 | 36808 |

### ctx_065536.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 64.1 | 100.0 | 233.8 | 305.1 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 58.7 | 100.0 | 226.1 | 299.6 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 57.8 | 100.0 | 232.3 | 288.8 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 58.7 | 100.0 | 238.9 | 283.5 | 36808 |

### ctx_100000.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 64.0 | 100.0 | 228.8 | 300.4 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 61.4 | 100.0 | 221.8 | 303.9 | 36808 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 59.7 | 100.0 | 229.0 | 287.6 | 38166 |
| 1 | NVIDIA RTX PRO 5000 Blackwell | Gen4 x16 | 63.3 | 100.0 | 229.0 | 287.1 | 36808 |

