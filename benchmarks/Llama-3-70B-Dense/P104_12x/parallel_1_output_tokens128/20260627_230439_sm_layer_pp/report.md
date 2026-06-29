# llama-server parallel-slots context benchmark report

## Test header

- MODEL: `/home/serg/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `131072`
- N_GEN: `128`
- BATCH: `4096`
- UBATCH: `32`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `5/7/7/7/7/7/7/7/7/7/7/6`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/projects/llama.cpp/bench_reports_Llama3_70B/20260627_230439/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
```

### nvidia_smi

```text
0, NVIDIA P104-100, 535.309.01, 8192 MiB
1, NVIDIA P104-100, 535.309.01, 8192 MiB
2, NVIDIA P104-100, 535.309.01, 8192 MiB
3, NVIDIA P104-100, 535.309.01, 8192 MiB
4, NVIDIA P104-100, 535.309.01, 8192 MiB
5, NVIDIA P104-100, 535.309.01, 8192 MiB
6, NVIDIA P104-100, 535.309.01, 8192 MiB
7, NVIDIA P104-100, 535.309.01, 8192 MiB
8, NVIDIA P104-100, 535.309.01, 8192 MiB
9, NVIDIA P104-100, 535.309.01, 8192 MiB
10, NVIDIA P104-100, 535.309.01, 8192 MiB
11, NVIDIA P104-100, 535.309.01, 8192 MiB
```

### nvcc

```text
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0
```

### cmake

```text
cmake version 3.28.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

## Server command

```bash
./build/bin/llama-server -m /home/serg/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 131072 --override-kv llama.context_length=int:131072 -b 4096 -ub 32 -np 1 -ctk f16 -sm layer -ts 5/7/7/7/7/7/7/7/7/7/7/6
```

## Summary

| File | Active slots | Request | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Decode time s | Wall s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 128 | 37.28 | 6.81 | 4.09 | 31.26 | 38.20 |
| ctx_000512.txt | 1 | 1 | 510 | 128 | 38.45 | 13.26 | 4.07 | 31.45 | 45.49 |
| ctx_001024.txt | 1 | 1 | 1022 | 128 | 38.41 | 26.61 | 4.08 | 31.34 | 59.19 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 37.99 | 53.86 | 4.05 | 31.59 | 88.05 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 36.77 | 111.36 | 3.94 | 32.51 | 147.84 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 21.0 | 43.4 | 44.5 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 11.3 | 27.0 | 87.5 | 179.4 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 13.7 | 41.0 | 48.3 | 51.5 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 17.8 | 46.0 | 49.1 | 55.0 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 15.7 | 41.0 | 46.9 | 51.6 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 4.7 | 28.0 | 63.9 | 126.9 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 6.2 | 37.0 | 65.5 | 166.5 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 6.0 | 36.0 | 48.0 | 51.7 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 72.3 | 176.7 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 57.5 | 76.5 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 10.5 | 43.0 | 45.4 | 50.2 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 9.5 | 29.0 | 42.3 | 42.4 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 5.9 | 10.0 | 49.5 | 103.2 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.6 | 13.0 | 55.3 | 120.2 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 7.0 | 12.0 | 51.7 | 142.7 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 7.2 | 12.0 | 62.9 | 162.2 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 12.0 | 48.3 | 108.5 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 9.1 | 12.0 | 49.3 | 108.1 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 12.0 | 58.0 | 113.8 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 12.0 | 52.7 | 112.4 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 8.5 | 12.0 | 67.0 | 160.1 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 12.0 | 58.9 | 143.5 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 7.6 | 13.0 | 50.5 | 113.9 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 9.6 | 14.0 | 48.2 | 73.3 | 6208 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 3.7 | 38.0 | 48.6 | 107.2 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 2.2 | 26.0 | 53.9 | 70.3 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 3.0 | 18.0 | 69.2 | 185.3 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 9.4 | 41.0 | 50.7 | 50.8 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 17.0 | 43.0 | 49.2 | 57.6 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 8.8 | 42.0 | 61.8 | 182.4 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 11.5 | 41.0 | 69.8 | 170.0 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 12.0 | 41.0 | 62.1 | 181.5 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 9.2 | 44.0 | 60.2 | 160.5 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 10.5 | 42.0 | 51.0 | 72.0 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 10.1 | 42.0 | 54.4 | 100.3 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 3.8 | 28.0 | 44.1 | 61.0 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 10.0 | 49.2 | 102.2 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.7 | 13.0 | 50.6 | 115.1 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 12.0 | 52.3 | 113.1 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 8.3 | 12.0 | 52.4 | 156.8 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 12.0 | 50.5 | 117.8 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 8.6 | 12.0 | 50.6 | 110.6 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 12.0 | 49.0 | 115.4 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 12.0 | 49.6 | 103.8 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 12.0 | 67.2 | 151.2 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 8.7 | 31.0 | 61.1 | 148.0 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 10.3 | 21.0 | 52.3 | 115.8 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 10.4 | 34.0 | 50.5 | 89.2 | 6208 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 39.0 | 44.6 | 68.8 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 7.1 | 44.0 | 58.6 | 189.3 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 5.7 | 43.0 | 56.7 | 165.7 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 5.9 | 42.0 | 64.5 | 167.9 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.8 | 42.0 | 61.6 | 178.9 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 11.3 | 42.0 | 49.4 | 54.7 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 9.7 | 42.0 | 57.4 | 186.9 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 11.2 | 42.0 | 64.8 | 175.6 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 13.1 | 42.0 | 55.1 | 81.6 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 11.6 | 42.0 | 61.0 | 146.6 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 3.4 | 42.0 | 53.6 | 115.8 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 3.5 | 29.0 | 47.4 | 97.0 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 7.1 | 10.0 | 54.8 | 110.0 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 7.2 | 13.0 | 57.9 | 122.1 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 13.0 | 49.2 | 119.5 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 12.0 | 55.8 | 109.2 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 12.0 | 50.5 | 118.4 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 8.4 | 42.0 | 64.7 | 129.8 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 8.6 | 42.0 | 67.3 | 154.0 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 9.4 | 42.0 | 53.2 | 108.8 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 6.0 | 12.0 | 62.7 | 168.7 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 8.8 | 12.0 | 54.1 | 139.2 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 9.8 | 30.0 | 48.9 | 115.6 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 20.0 | 51.1 | 114.7 | 6208 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.5 | 40.0 | 47.4 | 128.4 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 9.0 | 45.0 | 69.2 | 191.8 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 9.9 | 45.0 | 57.1 | 184.9 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 44.0 | 60.1 | 173.2 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 47.0 | 59.1 | 178.2 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 9.4 | 44.0 | 69.8 | 183.3 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 9.0 | 43.0 | 53.9 | 176.3 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 10.6 | 44.0 | 60.9 | 179.8 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 10.0 | 47.0 | 57.1 | 119.4 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 6.5 | 44.0 | 70.0 | 192.2 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 7.7 | 45.0 | 54.0 | 177.8 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 31.0 | 48.9 | 116.9 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 7.3 | 17.0 | 51.5 | 102.2 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 7.2 | 13.0 | 56.6 | 133.5 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 13.0 | 62.5 | 165.8 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 7.4 | 12.0 | 54.0 | 154.2 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 7.3 | 12.0 | 53.0 | 103.9 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 13.0 | 55.8 | 130.9 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 9.6 | 44.0 | 51.9 | 113.7 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 8.5 | 31.0 | 58.5 | 158.5 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 12.0 | 62.4 | 138.7 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 9.6 | 44.0 | 58.5 | 170.8 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 10.8 | 45.0 | 58.2 | 147.4 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 10.2 | 31.0 | 51.8 | 116.2 | 6208 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 8.3 | 64.0 | 53.0 | 173.4 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 10.1 | 49.0 | 59.3 | 188.9 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 49.0 | 59.8 | 179.5 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 7.2 | 90.0 | 65.7 | 183.1 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 48.0 | 58.5 | 169.6 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 9.0 | 48.0 | 59.4 | 185.3 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 7.6 | 47.0 | 59.6 | 182.8 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 9.4 | 65.0 | 62.6 | 174.5 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 10.9 | 47.0 | 62.0 | 181.7 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 7.6 | 47.0 | 61.9 | 193.2 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 48.0 | 60.1 | 179.2 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 5.9 | 59.0 | 48.7 | 114.8 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.4 | 10.0 | 52.3 | 94.5 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.5 | 14.0 | 59.8 | 119.8 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 10.2 | 47.0 | 54.9 | 117.2 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 8.7 | 48.0 | 47.9 | 111.9 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.6 | 48.0 | 46.3 | 63.4 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 9.0 | 13.0 | 48.5 | 93.6 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 47.0 | 54.4 | 150.9 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 7.2 | 20.0 | 54.8 | 146.2 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 8.2 | 34.0 | 65.2 | 177.9 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 9.2 | 48.0 | 58.0 | 118.7 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 14.0 | 48.9 | 94.5 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 10.2 | 37.0 | 47.2 | 86.7 | 6208 |

