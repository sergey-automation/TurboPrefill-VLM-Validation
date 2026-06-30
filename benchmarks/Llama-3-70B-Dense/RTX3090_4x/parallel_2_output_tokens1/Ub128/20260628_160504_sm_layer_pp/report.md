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
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_160504/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 2 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 508 | 1.11 | 456.20 |
| ctx_000512.txt | 2 | 1020 | 2.15 | 475.11 |
| ctx_001024.txt | 2 | 2044 | 4.55 | 448.80 |
| ctx_002048.txt | 2 | 4092 | 9.02 | 453.62 |
| ctx_004096.txt | 2 | 8188 | 18.50 | 442.49 |
| ctx_008192.txt | 2 | 16380 | 38.90 | 421.09 |
| ctx_016384.txt | 2 | 32764 | 85.17 | 384.69 |
| ctx_032768.txt | 2 | 65534 | 198.60 | 329.98 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 1 | 254 | 474.57 | 0.54 | 1.11 |
| ctx_000256.txt | 2 | 2 | 254 | 443.40 | 0.57 | 0.58 |
| ctx_000512.txt | 2 | 1 | 510 | 477.36 | 1.07 | 2.15 |
| ctx_000512.txt | 2 | 2 | 510 | 475.40 | 1.07 | 1.08 |
| ctx_001024.txt | 2 | 1 | 1022 | 239.53 | 4.27 | 4.55 |
| ctx_001024.txt | 2 | 2 | 1022 | 239.45 | 4.27 | 4.55 |
| ctx_002048.txt | 2 | 1 | 2046 | 236.62 | 8.65 | 9.02 |
| ctx_002048.txt | 2 | 2 | 2046 | 236.62 | 8.65 | 9.02 |
| ctx_004096.txt | 2 | 1 | 4094 | 230.32 | 17.78 | 18.50 |
| ctx_004096.txt | 2 | 2 | 4094 | 230.32 | 17.78 | 18.50 |
| ctx_008192.txt | 2 | 1 | 8190 | 218.56 | 37.47 | 38.90 |
| ctx_008192.txt | 2 | 2 | 8190 | 218.57 | 37.47 | 38.90 |
| ctx_016384.txt | 2 | 1 | 16382 | 198.97 | 82.34 | 85.17 |
| ctx_016384.txt | 2 | 2 | 16382 | 397.26 | 41.24 | 44.06 |
| ctx_032768.txt | 2 | 1 | 32767 | 215.57 | 152.00 | 198.59 |
| ctx_032768.txt | 2 | 2 | 32767 | 340.33 | 96.28 | 102.27 |

## GPU load during group response window

### ctx_000256.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 32.0 | 32.0 | 109.4 | 109.4 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 120.5 | 120.5 | 19278 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.6 | 109.6 | 19278 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 111.3 | 111.3 | 19646 |

### ctx_000512.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 34.5 | 48.0 | 128.9 | 131.4 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 146.2 | 146.2 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 135.9 | 135.9 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 135.9 | 135.9 | 19654 |

### ctx_001024.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.5 | 60.0 | 126.0 | 128.2 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.5 | 63.0 | 143.4 | 151.3 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.2 | 69.0 | 132.8 | 137.9 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 5.8 | 23.0 | 133.5 | 136.0 | 19654 |

### ctx_002048.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 28.0 | 61.0 | 123.8 | 133.4 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 10.2 | 44.0 | 141.9 | 148.7 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.4 | 70.0 | 132.2 | 141.1 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 65.0 | 131.7 | 138.8 | 19654 |

### ctx_004096.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.7 | 66.0 | 127.1 | 131.9 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 13.9 | 72.0 | 148.0 | 151.8 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.4 | 69.0 | 136.0 | 139.1 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.4 | 66.0 | 137.2 | 140.2 | 19654 |

### ctx_008192.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.0 | 73.0 | 128.2 | 134.5 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 34.9 | 84.0 | 149.4 | 157.0 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.7 | 78.0 | 135.1 | 143.1 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 15.1 | 76.0 | 135.6 | 141.6 | 19654 |

### ctx_016384.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.2 | 84.0 | 128.2 | 135.3 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.8 | 90.0 | 147.5 | 156.0 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.0 | 84.0 | 134.9 | 143.2 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.3 | 86.0 | 134.1 | 142.2 | 19654 |

### ctx_032768.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.6 | 95.0 | 127.7 | 137.1 | 17010 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.2 | 100.0 | 146.5 | 156.1 | 19286 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.6 | 100.0 | 134.9 | 144.9 | 19286 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.1 | 100.0 | 133.6 | 142.9 | 19654 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
