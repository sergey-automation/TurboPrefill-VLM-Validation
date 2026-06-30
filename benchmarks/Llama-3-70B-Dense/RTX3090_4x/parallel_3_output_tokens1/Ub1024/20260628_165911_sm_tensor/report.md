# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `1024`
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
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_165911/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 3 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 762 | 1.64 | 466.00 |
| ctx_000512.txt | 3 | 1530 | 2.58 | 592.32 |
| ctx_001024.txt | 3 | 3066 | 4.73 | 648.01 |
| ctx_002048.txt | 3 | 6138 | 9.61 | 638.89 |
| ctx_004096.txt | 3 | 12282 | 19.18 | 640.41 |
| ctx_008192.txt | 3 | 24570 | 39.13 | 627.85 |
| ctx_016384.txt | 3 | 49146 | 81.02 | 606.59 |
| ctx_032768.txt | 3 | 98301 | 173.54 | 566.45 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 1 | 254 | 263.97 | 0.96 | 1.63 |
| ctx_000256.txt | 3 | 2 | 254 | 381.99 | 0.66 | 0.67 |
| ctx_000256.txt | 3 | 3 | 254 | 263.56 | 0.96 | 1.63 |
| ctx_000512.txt | 3 | 1 | 510 | 209.79 | 2.43 | 2.58 |
| ctx_000512.txt | 3 | 2 | 510 | 209.91 | 2.43 | 2.58 |
| ctx_000512.txt | 3 | 3 | 510 | 210.04 | 2.43 | 2.58 |
| ctx_001024.txt | 3 | 1 | 1022 | 230.45 | 4.43 | 4.73 |
| ctx_001024.txt | 3 | 2 | 1022 | 230.51 | 4.43 | 4.73 |
| ctx_001024.txt | 3 | 3 | 1022 | 230.59 | 4.43 | 4.73 |
| ctx_002048.txt | 3 | 1 | 2046 | 226.69 | 9.03 | 9.60 |
| ctx_002048.txt | 3 | 2 | 2046 | 226.69 | 9.03 | 9.60 |
| ctx_002048.txt | 3 | 3 | 2046 | 226.70 | 9.03 | 9.61 |
| ctx_004096.txt | 3 | 1 | 4094 | 226.67 | 18.06 | 19.18 |
| ctx_004096.txt | 3 | 2 | 4094 | 226.66 | 18.06 | 19.18 |
| ctx_004096.txt | 3 | 3 | 4094 | 226.65 | 18.06 | 19.18 |
| ctx_008192.txt | 3 | 1 | 8190 | 221.64 | 36.95 | 39.13 |
| ctx_008192.txt | 3 | 2 | 8190 | 332.24 | 24.65 | 26.82 |
| ctx_008192.txt | 3 | 3 | 8190 | 332.27 | 24.65 | 26.82 |
| ctx_016384.txt | 3 | 1 | 16382 | 320.27 | 51.15 | 81.02 |
| ctx_016384.txt | 3 | 2 | 16382 | 639.27 | 25.63 | 29.86 |
| ctx_016384.txt | 3 | 3 | 16382 | 319.86 | 51.22 | 55.46 |
| ctx_032768.txt | 3 | 1 | 32767 | 386.03 | 84.88 | 173.53 |
| ctx_032768.txt | 3 | 2 | 32767 | 383.71 | 85.40 | 118.90 |
| ctx_032768.txt | 3 | 3 | 32767 | 595.05 | 55.07 | 63.79 |

## GPU load during group response window

### ctx_000256.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 59.0 | 100.0 | 117.1 | 130.8 | 14734 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 60.0 | 100.0 | 136.0 | 151.7 | 21242 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 57.0 | 100.0 | 125.9 | 141.6 | 21242 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.5 | 100.0 | 128.1 | 146.0 | 21242 |

### ctx_000512.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 66.7 | 100.0 | 135.2 | 149.7 | 14772 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 155.8 | 173.4 | 21280 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 145.0 | 162.4 | 21280 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 148.4 | 166.4 | 21280 |

### ctx_001024.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 75.0 | 100.0 | 134.7 | 148.3 | 14772 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 75.0 | 100.0 | 157.1 | 175.0 | 21280 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 75.0 | 100.0 | 145.8 | 163.3 | 21280 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 75.0 | 100.0 | 151.0 | 167.8 | 21280 |

### ctx_002048.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 86.4 | 100.0 | 140.0 | 149.9 | 14772 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.7 | 100.0 | 165.9 | 179.6 | 21280 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.7 | 100.0 | 153.4 | 166.5 | 21280 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.9 | 100.0 | 158.2 | 171.4 | 21280 |

### ctx_004096.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 86.8 | 100.0 | 144.1 | 150.6 | 14772 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.4 | 100.0 | 174.4 | 185.6 | 21280 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.4 | 100.0 | 159.6 | 168.8 | 21280 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.3 | 100.0 | 161.5 | 170.4 | 21280 |

### ctx_008192.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 89.7 | 100.0 | 146.8 | 153.0 | 14774 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.6 | 100.0 | 179.2 | 189.1 | 21282 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.7 | 100.0 | 162.7 | 172.2 | 21282 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.7 | 100.0 | 164.4 | 174.1 | 21282 |

### ctx_016384.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 91.2 | 100.0 | 147.0 | 153.5 | 14774 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 90.3 | 100.0 | 179.7 | 190.2 | 21282 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 89.7 | 100.0 | 164.1 | 174.2 | 21282 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 90.1 | 100.0 | 165.7 | 175.5 | 21282 |

### ctx_032768.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 91.7 | 100.0 | 148.9 | 155.6 | 14774 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 90.5 | 100.0 | 183.7 | 198.2 | 21282 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 90.2 | 100.0 | 167.0 | 179.4 | 21282 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 91.2 | 100.0 | 169.2 | 181.7 | 21282 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
