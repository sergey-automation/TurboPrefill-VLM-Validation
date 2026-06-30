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
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_153124/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 2 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 508 | 1.06 | 478.31 |
| ctx_000512.txt | 2 | 1020 | 1.98 | 514.52 |
| ctx_001024.txt | 2 | 2044 | 4.25 | 480.87 |
| ctx_002048.txt | 2 | 4092 | 8.39 | 487.95 |
| ctx_004096.txt | 2 | 8188 | 17.16 | 477.04 |
| ctx_008192.txt | 2 | 16380 | 35.79 | 457.71 |
| ctx_016384.txt | 2 | 32764 | 77.13 | 424.77 |
| ctx_032768.txt | 2 | 65534 | 176.30 | 371.72 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 2 | 1 | 254 | 464.43 | 0.55 | 0.55 |
| ctx_000256.txt | 2 | 2 | 254 | 498.19 | 0.51 | 1.06 |
| ctx_000512.txt | 2 | 1 | 510 | 515.97 | 0.99 | 1.98 |
| ctx_000512.txt | 2 | 2 | 510 | 516.08 | 0.99 | 0.99 |
| ctx_001024.txt | 2 | 1 | 1022 | 258.02 | 3.96 | 4.25 |
| ctx_001024.txt | 2 | 2 | 1022 | 257.94 | 3.96 | 4.25 |
| ctx_002048.txt | 2 | 1 | 2046 | 255.37 | 8.01 | 8.38 |
| ctx_002048.txt | 2 | 2 | 2046 | 255.38 | 8.01 | 8.38 |
| ctx_004096.txt | 2 | 1 | 4094 | 249.11 | 16.43 | 17.16 |
| ctx_004096.txt | 2 | 2 | 4094 | 249.12 | 16.43 | 17.16 |
| ctx_008192.txt | 2 | 1 | 8190 | 238.41 | 34.35 | 35.78 |
| ctx_008192.txt | 2 | 2 | 8190 | 238.41 | 34.35 | 35.79 |
| ctx_016384.txt | 2 | 1 | 16382 | 220.46 | 74.31 | 77.13 |
| ctx_016384.txt | 2 | 2 | 16382 | 440.02 | 37.23 | 40.05 |
| ctx_032768.txt | 2 | 1 | 32767 | 241.06 | 135.93 | 176.29 |
| ctx_032768.txt | 2 | 2 | 32767 | 384.37 | 85.25 | 91.22 |

## GPU load during group response window

### ctx_000256.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 30.0 | 30.0 | 109.4 | 109.4 | 18330 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 120.0 | 120.0 | 20136 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 108.7 | 108.7 | 20136 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 111.7 | 111.7 | 20592 |

### ctx_000512.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 58.0 | 100.0 | 135.3 | 143.8 | 18338 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 146.7 | 146.8 | 20156 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 136.7 | 139.2 | 20156 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 134.7 | 135.8 | 20612 |

### ctx_001024.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 124.6 | 156.8 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 152.3 | 184.0 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 132.7 | 168.6 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 4.2 | 17.0 | 129.5 | 164.8 | 20628 |

### ctx_002048.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.9 | 100.0 | 128.0 | 159.2 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.4 | 100.0 | 146.3 | 185.3 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.8 | 100.0 | 137.9 | 176.9 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 18.9 | 96.0 | 138.0 | 172.5 | 20628 |

### ctx_004096.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 18.9 | 100.0 | 128.3 | 166.6 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.3 | 100.0 | 151.7 | 188.1 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 15.3 | 100.0 | 135.4 | 179.6 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.3 | 100.0 | 133.9 | 160.8 | 20628 |

### ctx_008192.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 17.8 | 100.0 | 128.9 | 167.1 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.3 | 100.0 | 149.8 | 191.4 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.6 | 100.0 | 138.6 | 186.2 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.9 | 100.0 | 134.3 | 170.3 | 20628 |

### ctx_016384.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.0 | 100.0 | 129.3 | 180.6 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.2 | 100.0 | 152.3 | 206.3 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.6 | 100.0 | 136.2 | 195.2 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.6 | 100.0 | 135.4 | 186.8 | 20628 |

### ctx_032768.txt | active_slots=2

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.1 | 100.0 | 129.3 | 195.5 | 18354 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.0 | 100.0 | 151.7 | 227.1 | 20172 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.5 | 100.0 | 135.8 | 213.8 | 20172 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.5 | 100.0 | 134.0 | 197.8 | 20628 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
