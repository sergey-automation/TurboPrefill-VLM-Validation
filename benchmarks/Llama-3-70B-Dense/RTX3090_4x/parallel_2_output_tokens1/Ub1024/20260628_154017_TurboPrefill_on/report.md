# llama-server PARALLEL-only 1-token response benchmark report

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
- PARALLEL: `2`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `1`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_154017/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 2 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 508 | 1.02 | 499.48 |
| ctx_000512.txt | 2 | 1020 | 2.05 | 497.42 |
| ctx_001024.txt | 2 | 2044 | 4.10 | 498.29 |
| ctx_002048.txt | 2 | 4092 | 5.94 | 688.70 |
| ctx_004096.txt | 2 | 8188 | 9.30 | 880.16 |
| ctx_008192.txt | 2 | 16380 | 16.71 | 979.98 |
| ctx_016384.txt | 2 | 32764 | 37.21 | 880.43 |
| ctx_032768.txt | 2 | 65534 | 88.42 | 741.21 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 1 | 254 | 251.55 | 1.01 | 1.01 |
| ctx_000256.txt | 2 | 2 | 254 | 251.17 | 1.01 | 1.02 |
| ctx_000512.txt | 2 | 1 | 510 | 261.27 | 1.95 | 2.05 |
| ctx_000512.txt | 2 | 2 | 510 | 261.32 | 1.95 | 2.05 |
| ctx_001024.txt | 2 | 1 | 1022 | 261.41 | 3.91 | 4.10 |
| ctx_001024.txt | 2 | 2 | 1022 | 261.44 | 3.91 | 4.10 |
| ctx_002048.txt | 2 | 1 | 2046 | 367.78 | 5.56 | 5.94 |
| ctx_002048.txt | 2 | 2 | 2046 | 367.79 | 5.56 | 5.94 |
| ctx_004096.txt | 2 | 1 | 4094 | 477.35 | 8.58 | 9.30 |
| ctx_004096.txt | 2 | 2 | 4094 | 477.32 | 8.58 | 9.30 |
| ctx_008192.txt | 2 | 1 | 8190 | 535.73 | 15.29 | 16.71 |
| ctx_008192.txt | 2 | 2 | 8190 | 535.67 | 15.29 | 16.71 |
| ctx_016384.txt | 2 | 1 | 16382 | 948.88 | 17.26 | 20.09 |
| ctx_016384.txt | 2 | 2 | 16382 | 476.48 | 34.38 | 37.21 |
| ctx_032768.txt | 2 | 1 | 32767 | 489.56 | 66.93 | 88.41 |
| ctx_032768.txt | 2 | 2 | 32767 | 795.61 | 41.18 | 47.18 |

## GPU load during group response window

### ctx_000256.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 3.0 | 3.0 | 103.2 | 103.2 | 18338 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 117.5 | 117.5 | 20136 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 107.9 | 107.9 | 20136 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 108.8 | 108.8 | 20592 |

### ctx_000512.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 140.8 | 155.8 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 1.0 | 2.0 | 161.8 | 179.7 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 99.0 | 123.3 | 133.4 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 115.8 | 132.3 | 20628 |

### ctx_001024.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 25.0 | 100.0 | 125.5 | 155.5 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 14.2 | 57.0 | 148.3 | 182.9 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.2 | 100.0 | 144.4 | 161.4 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 132.9 | 157.9 | 20628 |

### ctx_002048.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 17.8 | 100.0 | 131.6 | 181.2 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.7 | 100.0 | 157.4 | 225.9 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 13.7 | 82.0 | 147.0 | 213.8 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 148.4 | 223.8 | 20628 |

### ctx_004096.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 35.8 | 100.0 | 145.1 | 212.7 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.3 | 100.0 | 170.2 | 235.1 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.4 | 100.0 | 161.6 | 225.9 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.0 | 100.0 | 151.4 | 224.2 | 20628 |

### ctx_008192.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 48.4 | 100.0 | 160.4 | 215.0 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.6 | 100.0 | 188.6 | 236.6 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.9 | 100.0 | 170.8 | 223.7 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 42.5 | 100.0 | 165.2 | 222.9 | 20628 |

### ctx_016384.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 38.2 | 100.0 | 154.5 | 209.4 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 56.4 | 100.0 | 184.0 | 236.6 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.1 | 100.0 | 167.7 | 221.4 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.8 | 100.0 | 163.6 | 231.9 | 20628 |

### ctx_032768.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 38.8 | 100.0 | 153.8 | 215.8 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.5 | 100.0 | 182.5 | 236.6 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 41.8 | 100.0 | 164.8 | 231.6 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.0 | 100.0 | 162.9 | 238.5 | 20628 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
