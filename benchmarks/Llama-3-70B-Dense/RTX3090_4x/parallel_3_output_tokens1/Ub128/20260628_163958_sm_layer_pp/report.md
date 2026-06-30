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
- PARALLEL: `3`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_163958/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 3 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 762 | 1.64 | 463.37 |
| ctx_000512.txt | 3 | 1530 | 3.39 | 450.78 |
| ctx_001024.txt | 3 | 3066 | 6.75 | 453.94 |
| ctx_002048.txt | 3 | 6138 | 13.62 | 450.63 |
| ctx_004096.txt | 3 | 12282 | 27.97 | 439.08 |
| ctx_008192.txt | 3 | 24570 | 57.96 | 423.91 |
| ctx_016384.txt | 3 | 49146 | 126.41 | 388.78 |
| ctx_032768.txt | 3 | 98301 | 295.16 | 333.05 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 1 | 254 | 238.48 | 1.07 | 1.64 |
| ctx_000256.txt | 3 | 2 | 254 | 238.82 | 1.06 | 1.64 |
| ctx_000256.txt | 3 | 3 | 254 | 443.35 | 0.57 | 0.58 |
| ctx_000512.txt | 3 | 1 | 510 | 155.02 | 3.29 | 3.39 |
| ctx_000512.txt | 3 | 2 | 510 | 154.90 | 3.29 | 3.39 |
| ctx_000512.txt | 3 | 3 | 510 | 154.97 | 3.29 | 3.39 |
| ctx_001024.txt | 3 | 1 | 1022 | 155.86 | 6.56 | 6.75 |
| ctx_001024.txt | 3 | 2 | 1022 | 155.89 | 6.56 | 6.75 |
| ctx_001024.txt | 3 | 3 | 1022 | 155.89 | 6.56 | 6.75 |
| ctx_002048.txt | 3 | 1 | 2046 | 154.50 | 13.24 | 13.62 |
| ctx_002048.txt | 3 | 2 | 2046 | 154.51 | 13.24 | 13.62 |
| ctx_002048.txt | 3 | 3 | 2046 | 154.49 | 13.24 | 13.62 |
| ctx_004096.txt | 3 | 1 | 4094 | 150.30 | 27.24 | 27.97 |
| ctx_004096.txt | 3 | 2 | 4094 | 150.30 | 27.24 | 27.97 |
| ctx_004096.txt | 3 | 3 | 4094 | 150.30 | 27.24 | 27.97 |
| ctx_008192.txt | 3 | 1 | 8190 | 144.89 | 56.53 | 57.96 |
| ctx_008192.txt | 3 | 2 | 8190 | 217.23 | 37.70 | 39.13 |
| ctx_008192.txt | 3 | 3 | 8190 | 217.24 | 37.70 | 39.13 |
| ctx_016384.txt | 3 | 1 | 16382 | 198.60 | 82.49 | 85.33 |
| ctx_016384.txt | 3 | 2 | 16382 | 397.51 | 41.21 | 44.05 |
| ctx_016384.txt | 3 | 3 | 16382 | 198.92 | 82.35 | 126.41 |
| ctx_032768.txt | 3 | 1 | 32767 | 215.31 | 152.19 | 198.80 |
| ctx_032768.txt | 3 | 2 | 32767 | 215.47 | 152.08 | 295.15 |
| ctx_032768.txt | 3 | 3 | 32767 | 340.27 | 96.30 | 102.31 |

## GPU load during group response window

### ctx_000256.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.0 | 32.0 | 118.5 | 130.9 | 17008 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 133.6 | 146.2 | 19310 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 124.6 | 139.4 | 19310 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 123.5 | 136.1 | 19678 |

### ctx_000512.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 18.0 | 46.0 | 122.0 | 133.2 | 17008 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 137.1 | 146.5 | 19310 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 1.3 | 3.0 | 129.7 | 139.5 | 19310 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 7.0 | 21.0 | 130.4 | 136.6 | 19678 |

### ctx_001024.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 25.7 | 62.0 | 128.2 | 132.0 | 17008 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 37.5 | 71.0 | 147.4 | 151.6 | 19310 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.3 | 70.0 | 135.1 | 138.2 | 19310 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.7 | 64.0 | 137.5 | 141.5 | 19678 |

### ctx_002048.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 16.5 | 61.0 | 128.9 | 132.5 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.6 | 71.0 | 148.4 | 152.8 | 19312 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.4 | 56.0 | 136.3 | 140.1 | 19312 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.8 | 64.0 | 137.3 | 140.5 | 19680 |

### ctx_004096.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 18.4 | 66.0 | 129.8 | 135.3 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.8 | 78.0 | 151.0 | 155.1 | 19312 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.8 | 75.0 | 136.8 | 142.7 | 19312 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.4 | 68.0 | 137.0 | 141.4 | 19680 |

### ctx_008192.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 16.0 | 72.0 | 128.6 | 134.2 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.3 | 81.0 | 149.8 | 156.4 | 19312 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 31.2 | 80.0 | 136.1 | 142.7 | 19312 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.9 | 76.0 | 136.4 | 141.7 | 19680 |

### ctx_016384.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 18.5 | 76.0 | 128.0 | 134.9 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.1 | 96.0 | 147.8 | 155.6 | 19312 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.8 | 95.0 | 135.6 | 143.3 | 19312 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.1 | 82.0 | 135.0 | 142.2 | 19680 |

### ctx_032768.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 21.7 | 100.0 | 127.5 | 137.1 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 100.0 | 147.0 | 157.5 | 19312 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 100.0 | 134.4 | 145.6 | 19312 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.8 | 100.0 | 133.8 | 143.2 | 19680 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
