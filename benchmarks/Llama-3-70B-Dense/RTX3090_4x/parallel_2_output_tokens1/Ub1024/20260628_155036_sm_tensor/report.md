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
- PARALLEL: `2`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_155036/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 2 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 508 | 1.09 | 467.14 |
| ctx_000512.txt | 2 | 1020 | 1.75 | 583.88 |
| ctx_001024.txt | 2 | 2044 | 3.57 | 573.03 |
| ctx_002048.txt | 2 | 4092 | 6.67 | 613.86 |
| ctx_004096.txt | 2 | 8188 | 13.21 | 619.95 |
| ctx_008192.txt | 2 | 16380 | 26.55 | 616.84 |
| ctx_016384.txt | 2 | 32764 | 55.24 | 593.13 |
| ctx_032768.txt | 2 | 65534 | 119.17 | 549.92 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 1 | 254 | 590.87 | 0.43 | 1.09 |
| ctx_000256.txt | 2 | 2 | 254 | 389.52 | 0.65 | 0.66 |
| ctx_000512.txt | 2 | 1 | 510 | 526.11 | 0.97 | 0.97 |
| ctx_000512.txt | 2 | 2 | 510 | 661.16 | 0.77 | 1.75 |
| ctx_001024.txt | 2 | 1 | 1022 | 326.49 | 3.13 | 3.57 |
| ctx_001024.txt | 2 | 2 | 1022 | 326.62 | 3.13 | 3.56 |
| ctx_002048.txt | 2 | 1 | 2046 | 336.13 | 6.09 | 6.66 |
| ctx_002048.txt | 2 | 2 | 2046 | 336.14 | 6.09 | 6.67 |
| ctx_004096.txt | 2 | 1 | 4094 | 338.62 | 12.09 | 13.21 |
| ctx_004096.txt | 2 | 2 | 4094 | 338.64 | 12.09 | 13.21 |
| ctx_008192.txt | 2 | 1 | 8190 | 335.72 | 24.40 | 26.55 |
| ctx_008192.txt | 2 | 2 | 8190 | 335.69 | 24.40 | 26.55 |
| ctx_016384.txt | 2 | 1 | 16382 | 321.14 | 51.01 | 55.24 |
| ctx_016384.txt | 2 | 2 | 16382 | 639.18 | 25.63 | 29.85 |
| ctx_032768.txt | 2 | 1 | 32767 | 382.61 | 85.64 | 119.17 |
| ctx_032768.txt | 2 | 2 | 32767 | 592.33 | 55.32 | 64.04 |

## GPU load during group response window

### ctx_000256.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 99.2 | 99.2 | 14740 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 113.9 | 113.9 | 21228 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 103.1 | 103.1 | 21228 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 102.8 | 102.8 | 21228 |

### ctx_000512.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 56.5 | 100.0 | 136.7 | 142.7 | 14824 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 157.3 | 162.1 | 21314 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 146.7 | 151.8 | 21316 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.5 | 97.0 | 153.6 | 158.3 | 21318 |

### ctx_001024.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 66.7 | 100.0 | 130.2 | 147.7 | 14884 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 150.0 | 173.0 | 21370 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 141.0 | 163.2 | 21370 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 144.7 | 166.7 | 21370 |

### ctx_002048.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 79.5 | 100.0 | 134.8 | 149.4 | 14884 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.0 | 100.0 | 157.6 | 175.7 | 21370 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.3 | 100.0 | 147.4 | 165.8 | 21370 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.2 | 100.0 | 151.0 | 168.9 | 21370 |

### ctx_004096.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 81.7 | 100.0 | 143.3 | 149.9 | 14884 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.3 | 100.0 | 170.1 | 180.2 | 21370 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.3 | 100.0 | 158.5 | 167.7 | 21370 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.4 | 100.0 | 162.2 | 172.2 | 21370 |

### ctx_008192.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 87.5 | 100.0 | 145.2 | 152.5 | 14884 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.5 | 100.0 | 175.7 | 188.4 | 21370 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.5 | 100.0 | 160.9 | 171.8 | 21370 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.2 | 100.0 | 162.5 | 173.7 | 21370 |

### ctx_016384.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.7 | 100.0 | 145.6 | 153.9 | 14884 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.4 | 100.0 | 177.4 | 189.0 | 21370 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.6 | 100.0 | 160.5 | 170.4 | 21370 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.5 | 100.0 | 163.8 | 174.3 | 21370 |

### ctx_032768.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 89.4 | 100.0 | 147.4 | 155.2 | 14884 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.8 | 100.0 | 180.9 | 195.2 | 21370 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 88.8 | 100.0 | 163.7 | 176.9 | 21370 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.8 | 100.0 | 166.8 | 180.2 | 21370 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
