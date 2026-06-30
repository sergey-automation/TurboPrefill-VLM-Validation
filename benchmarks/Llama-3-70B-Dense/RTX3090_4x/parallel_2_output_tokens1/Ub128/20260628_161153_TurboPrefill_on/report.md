# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `128`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `2`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `1`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_161153/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 2 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 508 | 1.11 | 455.77 |
| ctx_000512.txt | 2 | 1020 | 1.49 | 684.54 |
| ctx_001024.txt | 2 | 2044 | 2.11 | 970.13 |
| ctx_002048.txt | 2 | 4092 | 3.68 | 1112.86 |
| ctx_004096.txt | 2 | 8188 | 7.10 | 1153.87 |
| ctx_008192.txt | 2 | 16380 | 14.16 | 1156.60 |
| ctx_016384.txt | 2 | 32764 | 30.11 | 1088.17 |
| ctx_032768.txt | 2 | 65534 | 74.84 | 875.70 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 1 | 254 | 474.44 | 0.54 | 1.11 |
| ctx_000256.txt | 2 | 2 | 254 | 442.84 | 0.57 | 0.58 |
| ctx_000512.txt | 2 | 1 | 510 | 668.89 | 0.76 | 0.77 |
| ctx_000512.txt | 2 | 2 | 510 | 706.58 | 0.72 | 1.49 |
| ctx_001024.txt | 2 | 1 | 1022 | 561.98 | 1.82 | 2.11 |
| ctx_001024.txt | 2 | 2 | 1022 | 562.01 | 1.82 | 2.11 |
| ctx_002048.txt | 2 | 1 | 2046 | 617.58 | 3.31 | 3.68 |
| ctx_002048.txt | 2 | 2 | 2046 | 617.56 | 3.31 | 3.68 |
| ctx_004096.txt | 2 | 1 | 4094 | 642.92 | 6.37 | 7.09 |
| ctx_004096.txt | 2 | 2 | 4094 | 642.98 | 6.37 | 7.10 |
| ctx_008192.txt | 2 | 1 | 8190 | 643.08 | 12.74 | 14.16 |
| ctx_008192.txt | 2 | 2 | 8190 | 642.99 | 12.74 | 14.16 |
| ctx_016384.txt | 2 | 1 | 16382 | 600.52 | 27.28 | 30.11 |
| ctx_016384.txt | 2 | 2 | 16382 | 1193.82 | 13.72 | 16.55 |
| ctx_032768.txt | 2 | 1 | 32767 | 945.66 | 34.65 | 40.67 |
| ctx_032768.txt | 2 | 2 | 32767 | 590.41 | 55.50 | 74.83 |

## GPU load during group response window

### ctx_000256.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.0 | 23.0 | 108.9 | 108.9 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 121.6 | 121.6 | 19278 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.6 | 109.6 | 19278 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 112.0 | 112.0 | 19646 |

### ctx_000512.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 138.6 | 153.5 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.5 | 49.0 | 161.6 | 175.9 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 47.5 | 95.0 | 151.9 | 164.9 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.5 | 91.0 | 148.0 | 159.4 | 19654 |

### ctx_001024.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 32.0 | 64.0 | 145.4 | 185.4 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.5 | 73.0 | 157.8 | 195.4 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.0 | 72.0 | 145.7 | 182.9 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.5 | 77.0 | 140.2 | 170.1 | 19654 |

### ctx_002048.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 55.0 | 74.0 | 174.7 | 198.0 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 64.2 | 88.0 | 196.8 | 231.2 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.8 | 82.0 | 188.2 | 220.5 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.2 | 77.0 | 182.0 | 207.7 | 19654 |

### ctx_004096.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 49.7 | 74.0 | 168.7 | 201.4 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.1 | 85.0 | 197.4 | 234.5 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.1 | 82.0 | 183.0 | 220.4 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 41.0 | 76.0 | 176.4 | 210.2 | 19654 |

### ctx_008192.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 51.8 | 74.0 | 174.2 | 200.6 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 62.1 | 85.0 | 205.5 | 235.4 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 58.6 | 82.0 | 189.0 | 220.5 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.8 | 77.0 | 183.1 | 210.4 | 19654 |

### ctx_016384.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 50.0 | 75.0 | 172.4 | 203.9 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 58.4 | 90.0 | 201.7 | 237.2 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.0 | 83.0 | 186.1 | 220.8 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 51.2 | 77.0 | 181.4 | 213.1 | 19654 |

### ctx_032768.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 49.1 | 93.0 | 166.1 | 208.9 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.2 | 96.0 | 195.9 | 242.4 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 55.7 | 96.0 | 180.5 | 225.2 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.3 | 90.0 | 176.8 | 217.3 | 19654 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
