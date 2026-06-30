# llama-server PARALLEL-only 1-token response benchmark report

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
- PARALLEL: `3`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_165026/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 3 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 762 | 1.87 | 407.13 |
| ctx_000512.txt | 3 | 1530 | 3.49 | 437.90 |
| ctx_001024.txt | 3 | 3066 | 8.11 | 378.20 |
| ctx_002048.txt | 3 | 6138 | 12.15 | 505.28 |
| ctx_004096.txt | 3 | 12282 | 24.16 | 508.35 |
| ctx_008192.txt | 3 | 24570 | 52.07 | 471.88 |
| ctx_016384.txt | 3 | 49146 | 109.46 | 448.97 |
| ctx_032768.txt | 3 | 98301 | 227.73 | 431.65 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 1 | 254 | 223.18 | 1.14 | 1.87 |
| ctx_000256.txt | 3 | 2 | 254 | 223.48 | 1.14 | 1.87 |
| ctx_000256.txt | 3 | 3 | 254 | 349.50 | 0.73 | 0.73 |
| ctx_000512.txt | 3 | 1 | 510 | 247.71 | 2.06 | 3.49 |
| ctx_000512.txt | 3 | 2 | 510 | 398.33 | 1.28 | 1.29 |
| ctx_000512.txt | 3 | 3 | 510 | 247.53 | 2.06 | 3.49 |
| ctx_001024.txt | 3 | 1 | 1022 | 196.52 | 5.20 | 8.11 |
| ctx_001024.txt | 3 | 2 | 1022 | 196.53 | 5.20 | 8.10 |
| ctx_001024.txt | 3 | 3 | 1022 | 391.40 | 2.61 | 2.62 |
| ctx_002048.txt | 3 | 1 | 2046 | 176.95 | 11.56 | 12.15 |
| ctx_002048.txt | 3 | 2 | 2046 | 176.95 | 11.56 | 12.15 |
| ctx_002048.txt | 3 | 3 | 2046 | 176.95 | 11.56 | 12.14 |
| ctx_004096.txt | 3 | 1 | 4094 | 177.71 | 23.04 | 24.16 |
| ctx_004096.txt | 3 | 2 | 4094 | 177.70 | 23.04 | 24.16 |
| ctx_004096.txt | 3 | 3 | 4094 | 177.70 | 23.04 | 24.16 |
| ctx_008192.txt | 3 | 1 | 8190 | 259.63 | 31.54 | 33.72 |
| ctx_008192.txt | 3 | 2 | 8190 | 259.65 | 31.54 | 33.72 |
| ctx_008192.txt | 3 | 3 | 8190 | 164.17 | 49.89 | 52.06 |
| ctx_016384.txt | 3 | 1 | 16382 | 232.20 | 70.55 | 74.79 |
| ctx_016384.txt | 3 | 2 | 16382 | 234.41 | 69.88 | 109.46 |
| ctx_016384.txt | 3 | 3 | 16382 | 463.56 | 35.34 | 39.57 |
| ctx_032768.txt | 3 | 1 | 32767 | 295.43 | 110.91 | 227.73 |
| ctx_032768.txt | 3 | 2 | 32767 | 295.19 | 111.00 | 154.65 |
| ctx_032768.txt | 3 | 3 | 32767 | 449.33 | 72.92 | 81.64 |

## GPU load during group response window

### ctx_000256.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 50.0 | 100.0 | 113.6 | 123.7 | 14072 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 132.0 | 143.9 | 20582 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.0 | 96.0 | 122.0 | 133.9 | 20586 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.5 | 91.0 | 123.7 | 137.3 | 20588 |

### ctx_000512.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 62.0 | 100.0 | 127.1 | 131.4 | 14166 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 65.0 | 98.0 | 145.6 | 149.0 | 20674 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.0 | 100.0 | 135.0 | 139.6 | 20674 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 137.5 | 144.2 | 20674 |

### ctx_001024.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 68.7 | 100.0 | 122.4 | 130.0 | 14464 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 68.4 | 100.0 | 143.8 | 153.6 | 20972 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 68.7 | 100.0 | 132.1 | 143.2 | 20972 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 72.0 | 100.0 | 135.2 | 146.3 | 20972 |

### ctx_002048.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 89.5 | 100.0 | 135.8 | 143.8 | 14498 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 89.1 | 100.0 | 160.2 | 171.1 | 21006 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 89.0 | 100.0 | 148.0 | 157.9 | 21006 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 90.4 | 100.0 | 151.5 | 161.4 | 21006 |

### ctx_004096.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 89.5 | 100.0 | 139.5 | 144.9 | 14500 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.6 | 100.0 | 168.3 | 177.7 | 21008 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.4 | 100.0 | 153.6 | 161.3 | 21008 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.1 | 100.0 | 155.4 | 162.3 | 21008 |

### ctx_008192.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 86.6 | 100.0 | 137.3 | 145.1 | 14870 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.7 | 100.0 | 166.3 | 177.7 | 21378 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.0 | 100.0 | 151.3 | 162.6 | 21378 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.9 | 100.0 | 152.3 | 162.8 | 21378 |

### ctx_016384.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 84.5 | 100.0 | 138.2 | 144.7 | 14986 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.5 | 100.0 | 166.7 | 178.6 | 21476 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.4 | 100.0 | 153.2 | 164.7 | 21504 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.8 | 100.0 | 153.8 | 164.8 | 21504 |

### ctx_032768.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.5 | 100.0 | 140.7 | 148.8 | 14998 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.2 | 100.0 | 172.6 | 189.6 | 21506 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.4 | 100.0 | 159.1 | 175.4 | 21504 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.6 | 100.0 | 159.3 | 174.0 | 21506 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
