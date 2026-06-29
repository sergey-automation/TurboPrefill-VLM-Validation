# llama-server context benchmark report

## Test header

- MODEL: `/home/serg/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `131072`
- N_GEN: `128`
- BATCH: `4096`
- UBATCH: `32`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `5/7/7/7/7/7/7/7/7/7/7/6`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- TURBOPREFILL: `0`
- llama_server_log: `/home/serg/workspace/projects/llama.cpp/bench_reports_Llama3_70B/20260627_081100/llama_server.log`

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
./build/bin/llama-server -m /home/serg/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 131072 --override-kv llama.context_length=int:131072 -b 4096 -ub 32 -np 1 -ctk f16 -sm tensor -ts 5/7/7/7/7/7/7/7/7/7/7/6
```

## Summary

| File | Prompt tokens | Completion tokens | Prefill tok/s | Prefill time s | Decode tok/s | Wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 254 | 128 | 1.18 | 215.76 | 0.96 | 349.36 |
| ctx_000512.txt | 510 | 128 | 1.18 | 432.23 | 0.96 | 566.30 |

## GPU load by stage

### ctx_000256.txt

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 58.4 | 67.0 | 54.6 | 57.2 | 5057 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 54.4 | 61.0 | 55.2 | 60.7 | 7042 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 54.6 | 59.0 | 53.1 | 58.6 | 6982 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 47.1 | 51.0 | 51.7 | 54.8 | 7478 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 41.2 | 47.0 | 52.9 | 58.4 | 7042 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 22.0 | 43.4 | 48.1 | 6984 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 18.5 | 22.0 | 41.9 | 47.9 | 7476 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 23.0 | 43.2 | 46.7 | 6964 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 12.0 | 45.7 | 55.2 | 7508 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 8.0 | 44.1 | 48.8 | 6978 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 8.0 | 44.2 | 54.8 | 6936 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 6.5 | 10.0 | 44.5 | 54.6 | 6196 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 58.3 | 60.0 | 56.8 | 59.5 | 5057 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 59.4 | 62.0 | 58.2 | 62.0 | 7042 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 57.8 | 60.0 | 55.8 | 58.6 | 6982 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 49.5 | 51.0 | 54.6 | 58.8 | 7478 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 44.9 | 47.0 | 55.6 | 59.1 | 7042 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 19.0 | 44.6 | 46.4 | 6984 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 19.0 | 43.1 | 47.2 | 7476 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 18.5 | 19.0 | 44.7 | 46.7 | 6964 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 9.0 | 47.3 | 49.9 | 7508 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 9.0 | 45.8 | 47.9 | 6978 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 9.0 | 44.2 | 46.8 | 6936 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 8.0 | 44.9 | 46.4 | 6196 |

### ctx_000512.txt

Prefill stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 58.4 | 66.0 | 55.0 | 60.1 | 5057 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 54.4 | 61.0 | 55.4 | 63.9 | 7042 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 54.9 | 63.0 | 53.1 | 57.2 | 6982 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 47.1 | 51.0 | 51.8 | 56.1 | 7478 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 41.1 | 46.0 | 53.1 | 59.3 | 7042 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 18.6 | 21.0 | 42.9 | 47.1 | 6984 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 25.0 | 41.3 | 45.1 | 7476 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 18.6 | 23.0 | 43.2 | 46.4 | 6964 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 10.0 | 45.4 | 49.9 | 7508 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 10.0 | 44.0 | 48.3 | 6978 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 6.7 | 10.0 | 42.7 | 46.4 | 6936 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 6.6 | 12.0 | 43.5 | 46.7 | 6196 |

Decode stage:

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA P104-100 | Gen1 x1 | 58.5 | 60.0 | 57.0 | 59.7 | 5057 |
| 1 | NVIDIA P104-100 | Gen1 x1 | 59.7 | 62.0 | 58.7 | 65.0 | 7042 |
| 2 | NVIDIA P104-100 | Gen1 x1 | 58.1 | 60.0 | 55.8 | 59.8 | 6982 |
| 3 | NVIDIA P104-100 | Gen1 x1 | 49.6 | 51.0 | 54.7 | 57.7 | 7478 |
| 4 | NVIDIA P104-100 | Gen1 x1 | 45.1 | 47.0 | 55.8 | 59.8 | 7042 |
| 5 | NVIDIA P104-100 | Gen1 x1 | 18.7 | 19.0 | 44.5 | 45.9 | 6984 |
| 6 | NVIDIA P104-100 | Gen1 x1 | 18.9 | 19.0 | 43.2 | 45.3 | 7476 |
| 7 | NVIDIA P104-100 | Gen1 x1 | 18.6 | 19.0 | 44.8 | 46.4 | 6964 |
| 8 | NVIDIA P104-100 | Gen1 x1 | 8.1 | 9.0 | 47.3 | 49.7 | 7508 |
| 9 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 9.0 | 45.9 | 48.0 | 6978 |
| 10 | NVIDIA P104-100 | Gen1 x1 | 8.0 | 9.0 | 44.3 | 47.8 | 6936 |
| 11 | NVIDIA P104-100 | Gen1 x1 | 7.8 | 8.0 | 45.0 | 47.3 | 6196 |

