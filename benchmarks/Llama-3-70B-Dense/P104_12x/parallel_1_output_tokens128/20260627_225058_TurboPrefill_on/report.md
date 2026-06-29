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
- TURBOPREFILL: `1`
- Parallel-slots mode: `active_slots=1..PARALLEL`
- Metrics policy: `server per-request timings only; no combined throughput calculated`
- llama_server_log: `/home/serg/workspace/projects/llama.cpp/bench_reports_Llama3_70B/20260627_225058/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
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
| ctx_000256.txt | 1 | 1 | 254 | 128 | 91.38 | 2.78 | 4.07 | 31.42 | 34.33 |
| ctx_000512.txt | 1 | 1 | 510 | 106 | 139.82 | 3.65 | 4.14 | 25.58 | 30.01 |
| ctx_001024.txt | 1 | 1 | 1022 | 50 | 173.77 | 5.88 | 4.24 | 11.79 | 18.89 |
| ctx_002048.txt | 1 | 1 | 2046 | 128 | 192.85 | 10.61 | 4.02 | 31.88 | 44.67 |
| ctx_004096.txt | 1 | 1 | 4094 | 128 | 199.32 | 20.54 | 3.94 | 32.46 | 56.98 |

## GPU load by stage

### ctx_000256.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 10.7 | 32.0 | 49.5 | 52.8 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 33.0 | 57.0 | 49.7 | 53.0 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 34.0 | 61.0 | 49.2 | 54.3 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 16.3 | 49.0 | 48.4 | 53.0 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 18.3 | 55.0 | 89.3 | 173.0 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 20.3 | 61.0 | 49.0 | 52.5 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 21.7 | 65.0 | 47.1 | 50.6 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 14.0 | 42.0 | 59.7 | 86.1 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 17.0 | 51.0 | 66.9 | 103.4 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 95.1 | 179.1 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 44.5 | 50.4 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 0.0 | 0.0 | 45.0 | 51.0 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.9 | 10.0 | 49.7 | 103.8 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 9.8 | 13.0 | 54.1 | 120.7 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 12.0 | 52.9 | 115.4 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 6.8 | 12.0 | 50.0 | 158.1 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 12.0 | 50.1 | 101.8 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 7.5 | 13.0 | 51.8 | 113.8 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 12.0 | 48.4 | 103.9 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 12.0 | 52.7 | 115.0 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 12.0 | 65.0 | 162.8 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 7.6 | 12.0 | 57.5 | 110.2 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 8.3 | 13.0 | 51.8 | 110.3 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 10.1 | 14.0 | 53.1 | 103.5 | 6208 |

### ctx_000512.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 41.7 | 73.0 | 52.2 | 59.4 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 54.0 | 90.0 | 54.2 | 63.8 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 54.7 | 92.0 | 73.7 | 125.5 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 31.0 | 50.0 | 79.0 | 148.3 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 40.3 | 71.0 | 96.2 | 164.9 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 14.3 | 43.0 | 111.5 | 179.1 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 15.0 | 45.0 | 86.8 | 178.6 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 56.0 | 75.2 | 141.0 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 20.7 | 62.0 | 55.7 | 78.3 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 18.0 | 54.0 | 48.9 | 58.7 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 19.3 | 58.0 | 45.6 | 53.1 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 8.3 | 25.0 | 45.5 | 51.8 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 7.5 | 21.0 | 54.7 | 91.9 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 13.0 | 61.1 | 155.0 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 7.7 | 12.0 | 60.6 | 159.8 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 9.5 | 12.0 | 58.7 | 142.1 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 7.3 | 12.0 | 52.0 | 90.3 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 6.4 | 12.0 | 54.8 | 114.2 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 6.1 | 12.0 | 57.8 | 153.9 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 12.0 | 57.6 | 151.3 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 12.0 | 64.1 | 135.0 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 12.0 | 62.1 | 147.0 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 9.7 | 13.0 | 59.7 | 145.6 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 6.5 | 14.0 | 57.3 | 147.7 | 6208 |

### ctx_001024.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 32.0 | 65.0 | 81.5 | 185.5 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 34.5 | 74.0 | 57.4 | 87.2 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 37.0 | 75.0 | 54.2 | 78.9 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 26.2 | 53.0 | 60.7 | 109.5 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 33.5 | 72.0 | 83.4 | 131.1 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 26.8 | 58.0 | 111.0 | 185.3 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 27.2 | 59.0 | 90.2 | 177.0 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 29.8 | 61.0 | 82.8 | 172.7 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 29.2 | 62.0 | 86.3 | 176.8 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 36.2 | 62.0 | 62.2 | 104.6 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 36.2 | 62.0 | 53.6 | 78.9 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 20.0 | 36.0 | 76.2 | 168.3 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 2.5 | 9.0 | 65.8 | 136.0 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 10.8 | 13.0 | 58.4 | 107.1 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 12.0 | 58.9 | 112.0 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 7.1 | 12.0 | 64.8 | 126.6 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 8.8 | 12.0 | 64.1 | 134.9 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 11.2 | 15.0 | 57.8 | 102.7 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 14.6 | 55.0 | 55.2 | 88.2 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 14.1 | 67.0 | 66.2 | 152.5 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 16.8 | 82.0 | 79.3 | 173.3 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 12.4 | 68.0 | 75.8 | 178.5 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 12.9 | 68.0 | 67.0 | 178.2 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 12.7 | 51.0 | 64.3 | 112.8 | 6208 |

### ctx_002048.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 39.4 | 67.0 | 76.5 | 158.2 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 42.1 | 75.0 | 88.1 | 171.4 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 42.2 | 74.0 | 83.8 | 181.4 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 35.2 | 65.0 | 83.1 | 177.5 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 39.8 | 73.0 | 90.8 | 178.7 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 30.4 | 51.0 | 85.2 | 176.8 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 30.2 | 54.0 | 83.4 | 180.6 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 39.2 | 61.0 | 93.0 | 176.6 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 34.1 | 59.0 | 100.1 | 190.9 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 33.0 | 60.0 | 99.8 | 179.8 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 34.0 | 60.0 | 101.3 | 178.1 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 18.6 | 41.0 | 84.6 | 130.9 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 6.0 | 10.0 | 52.6 | 106.8 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 7.6 | 13.0 | 55.4 | 127.7 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 17.0 | 49.6 | 115.0 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 8.9 | 47.0 | 49.9 | 100.6 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 10.8 | 63.0 | 56.2 | 113.7 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 11.7 | 62.0 | 52.8 | 110.3 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 10.4 | 67.0 | 51.1 | 133.3 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 9.6 | 51.0 | 54.8 | 128.9 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 9.8 | 71.0 | 65.5 | 151.1 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 9.1 | 56.0 | 62.9 | 173.9 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 10.5 | 59.0 | 54.6 | 153.4 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 10.9 | 47.0 | 56.2 | 162.2 | 6208 |

### ctx_004096.txt | active_slots=1 | request=1

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 48.1 | 80.0 | 65.5 | 158.4 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 51.4 | 84.0 | 70.0 | 173.5 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 53.4 | 83.0 | 69.5 | 170.6 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 43.5 | 62.0 | 73.7 | 176.6 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 54.5 | 76.0 | 98.9 | 179.6 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 35.2 | 60.0 | 124.9 | 187.2 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 37.7 | 60.0 | 115.0 | 187.6 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 39.2 | 69.0 | 110.8 | 178.4 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 39.3 | 60.0 | 116.3 | 195.8 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 36.7 | 59.0 | 108.7 | 186.3 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 36.4 | 60.0 | 92.1 | 180.7 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 24.4 | 41.0 | 65.7 | 173.0 | 6208 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 7.9 | 67.0 | 50.0 | 108.2 | 5495 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 9.8 | 70.0 | 49.5 | 88.5 | 7326 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 10.5 | 70.0 | 51.8 | 137.6 | 7208 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 11.3 | 57.0 | 53.2 | 154.6 | 7150 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 11.4 | 64.0 | 60.3 | 177.1 | 7150 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 11.2 | 73.0 | 70.4 | 178.1 | 7208 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 10.5 | 61.0 | 56.7 | 126.8 | 7150 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 10.9 | 73.0 | 52.8 | 136.2 | 7150 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 10.4 | 54.0 | 63.3 | 163.6 | 7208 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 10.1 | 59.0 | 55.0 | 169.4 | 7150 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 12.7 | 75.0 | 52.3 | 163.3 | 7384 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 10.6 | 39.0 | 55.9 | 165.1 | 6208 |

