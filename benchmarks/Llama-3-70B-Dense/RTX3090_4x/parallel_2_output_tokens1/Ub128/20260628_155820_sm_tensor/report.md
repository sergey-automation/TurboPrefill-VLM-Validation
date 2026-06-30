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
- PARALLEL: `2`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_155820/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 2 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 508 | 1.19 | 428.11 |
| ctx_000512.txt | 2 | 1020 | 2.05 | 498.12 |
| ctx_001024.txt | 2 | 2044 | 4.20 | 486.31 |
| ctx_002048.txt | 2 | 4092 | 8.19 | 499.72 |
| ctx_004096.txt | 2 | 8188 | 16.43 | 498.23 |
| ctx_008192.txt | 2 | 16380 | 33.27 | 492.28 |
| ctx_016384.txt | 2 | 32764 | 75.16 | 435.94 |
| ctx_032768.txt | 2 | 65534 | 153.01 | 428.30 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 1 | 254 | 215.20 | 1.18 | 1.19 |
| ctx_000256.txt | 2 | 2 | 254 | 214.93 | 1.18 | 1.19 |
| ctx_000512.txt | 2 | 1 | 510 | 269.11 | 1.90 | 2.05 |
| ctx_000512.txt | 2 | 2 | 510 | 269.30 | 1.89 | 2.05 |
| ctx_001024.txt | 2 | 1 | 1022 | 261.45 | 3.91 | 4.20 |
| ctx_001024.txt | 2 | 2 | 1022 | 261.36 | 3.91 | 4.20 |
| ctx_002048.txt | 2 | 1 | 2046 | 268.31 | 7.63 | 8.19 |
| ctx_002048.txt | 2 | 2 | 2046 | 268.31 | 7.63 | 8.19 |
| ctx_004096.txt | 2 | 1 | 4094 | 267.43 | 15.31 | 16.43 |
| ctx_004096.txt | 2 | 2 | 4094 | 267.44 | 15.31 | 16.43 |
| ctx_008192.txt | 2 | 1 | 8190 | 263.20 | 31.12 | 33.27 |
| ctx_008192.txt | 2 | 2 | 8190 | 263.18 | 31.12 | 33.27 |
| ctx_016384.txt | 2 | 1 | 16382 | 451.49 | 36.28 | 40.51 |
| ctx_016384.txt | 2 | 2 | 16382 | 230.98 | 70.92 | 75.16 |
| ctx_032768.txt | 2 | 1 | 32767 | 298.93 | 109.62 | 153.00 |
| ctx_032768.txt | 2 | 2 | 32767 | 453.88 | 72.19 | 80.94 |

## GPU load during group response window

### ctx_000256.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 102.5 | 102.5 | 14034 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 118.3 | 118.3 | 20522 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 108.4 | 108.4 | 20522 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.5 | 109.5 | 20522 |

### ctx_000512.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 48.0 | 96.0 | 118.8 | 137.5 | 14114 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 133.8 | 159.9 | 20602 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 124.5 | 150.8 | 20602 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.0 | 83.0 | 125.0 | 150.7 | 20602 |

### ctx_001024.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 75.0 | 100.0 | 133.3 | 141.2 | 14250 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 73.0 | 100.0 | 154.6 | 164.2 | 20742 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 71.0 | 100.0 | 146.0 | 154.4 | 20744 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 70.0 | 98.0 | 146.9 | 157.2 | 20746 |

### ctx_002048.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.6 | 100.0 | 135.3 | 142.2 | 14452 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.2 | 100.0 | 158.2 | 167.2 | 20938 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.8 | 100.0 | 148.0 | 156.4 | 20938 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.8 | 100.0 | 150.7 | 159.8 | 20938 |

### ctx_004096.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.3 | 100.0 | 135.5 | 143.0 | 14558 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.9 | 100.0 | 159.2 | 169.4 | 21046 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.9 | 100.0 | 149.7 | 159.1 | 21046 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.3 | 100.0 | 151.8 | 161.7 | 21046 |

### ctx_008192.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 86.8 | 100.0 | 138.4 | 144.3 | 14574 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.8 | 100.0 | 166.7 | 179.0 | 21060 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 87.9 | 100.0 | 153.4 | 163.1 | 21050 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 86.5 | 100.0 | 154.9 | 163.6 | 21048 |

### ctx_016384.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 82.4 | 100.0 | 136.7 | 145.3 | 14960 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.0 | 100.0 | 165.2 | 178.6 | 21448 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.6 | 100.0 | 151.1 | 164.2 | 21448 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 79.4 | 100.0 | 151.7 | 164.7 | 21448 |

### ctx_032768.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 86.9 | 100.0 | 141.0 | 149.1 | 14978 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.4 | 100.0 | 172.2 | 189.7 | 21468 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.2 | 100.0 | 156.5 | 172.0 | 21472 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 85.1 | 100.0 | 158.8 | 173.7 | 21472 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
