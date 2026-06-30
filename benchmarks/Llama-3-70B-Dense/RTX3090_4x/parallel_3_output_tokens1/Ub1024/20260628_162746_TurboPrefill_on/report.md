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
- PARALLEL: `3`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `1`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_162746/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 3 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 762 | 1.46 | 521.33 |
| ctx_000512.txt | 3 | 1530 | 3.05 | 501.06 |
| ctx_001024.txt | 3 | 3066 | 6.14 | 499.32 |
| ctx_002048.txt | 3 | 6138 | 12.44 | 493.53 |
| ctx_004096.txt | 3 | 12282 | 25.64 | 479.08 |
| ctx_008192.txt | 3 | 24570 | 26.37 | 931.87 |
| ctx_016384.txt | 3 | 49146 | 53.75 | 914.29 |
| ctx_032768.txt | 3 | 98301 | 127.35 | 771.91 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 1 | 254 | 174.78 | 1.45 | 1.46 |
| ctx_000256.txt | 3 | 2 | 254 | 174.95 | 1.45 | 1.46 |
| ctx_000256.txt | 3 | 3 | 254 | 174.58 | 1.45 | 1.46 |
| ctx_000512.txt | 3 | 1 | 510 | 172.89 | 2.95 | 3.05 |
| ctx_000512.txt | 3 | 2 | 510 | 172.86 | 2.95 | 3.05 |
| ctx_000512.txt | 3 | 3 | 510 | 172.90 | 2.95 | 3.05 |
| ctx_001024.txt | 3 | 1 | 1022 | 172.02 | 5.94 | 6.14 |
| ctx_001024.txt | 3 | 2 | 1022 | 172.02 | 5.94 | 6.14 |
| ctx_001024.txt | 3 | 3 | 1022 | 172.00 | 5.94 | 6.14 |
| ctx_002048.txt | 3 | 1 | 2046 | 169.61 | 12.06 | 12.43 |
| ctx_002048.txt | 3 | 2 | 2046 | 169.61 | 12.06 | 12.43 |
| ctx_002048.txt | 3 | 3 | 2046 | 169.60 | 12.06 | 12.44 |
| ctx_004096.txt | 3 | 1 | 4094 | 164.40 | 24.90 | 25.64 |
| ctx_004096.txt | 3 | 2 | 4094 | 164.40 | 24.90 | 25.63 |
| ctx_004096.txt | 3 | 3 | 4094 | 164.40 | 24.90 | 25.63 |
| ctx_008192.txt | 3 | 1 | 8190 | 524.13 | 15.63 | 17.05 |
| ctx_008192.txt | 3 | 2 | 8190 | 328.43 | 24.94 | 26.36 |
| ctx_008192.txt | 3 | 3 | 8190 | 524.08 | 15.63 | 17.05 |
| ctx_016384.txt | 3 | 1 | 16382 | 965.42 | 16.97 | 19.80 |
| ctx_016384.txt | 3 | 2 | 16382 | 481.64 | 34.01 | 36.85 |
| ctx_016384.txt | 3 | 3 | 16382 | 482.64 | 33.94 | 53.75 |
| ctx_032768.txt | 3 | 1 | 32767 | 498.43 | 65.74 | 86.90 |
| ctx_032768.txt | 3 | 2 | 32767 | 812.27 | 40.34 | 46.34 |
| ctx_032768.txt | 3 | 3 | 32767 | 498.92 | 65.68 | 127.34 |

## GPU load during group response window

### ctx_000256.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 2.0 | 4.0 | 121.0 | 137.3 | 18066 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 138.8 | 157.7 | 20060 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 34.5 | 69.0 | 127.8 | 147.1 | 20060 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 40.0 | 80.0 | 110.2 | 110.5 | 20516 |

### ctx_000512.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 33.3 | 100.0 | 125.4 | 159.2 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 37.0 | 67.0 | 143.1 | 185.2 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.3 | 67.0 | 117.6 | 145.4 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.7 | 2.0 | 127.6 | 159.3 | 20530 |

### ctx_001024.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 33.3 | 100.0 | 125.9 | 156.8 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.7 | 100.0 | 149.5 | 183.8 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 18.3 | 100.0 | 140.1 | 176.1 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 15.5 | 93.0 | 131.6 | 164.7 | 20530 |

### ctx_002048.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 15.5 | 100.0 | 129.4 | 158.9 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 34.2 | 100.0 | 149.4 | 185.8 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.3 | 100.0 | 133.0 | 177.2 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.8 | 100.0 | 136.7 | 170.9 | 20530 |

### ctx_004096.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.0 | 100.0 | 127.5 | 161.7 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.1 | 100.0 | 151.2 | 190.6 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.6 | 100.0 | 141.0 | 181.3 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.4 | 100.0 | 135.8 | 168.2 | 20530 |

### ctx_008192.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 45.9 | 100.0 | 160.0 | 220.5 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 59.2 | 100.0 | 191.3 | 237.3 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 53.9 | 100.0 | 170.8 | 228.5 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.7 | 100.0 | 167.6 | 220.7 | 20530 |

### ctx_016384.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 45.0 | 100.0 | 158.7 | 216.5 | 18082 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.1 | 100.0 | 188.0 | 239.3 | 20076 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 49.8 | 100.0 | 169.3 | 227.6 | 20076 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.0 | 100.0 | 166.7 | 231.8 | 20532 |

### ctx_032768.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 40.2 | 100.0 | 156.3 | 213.7 | 18082 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 51.0 | 100.0 | 185.5 | 237.8 | 20076 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 46.1 | 100.0 | 168.2 | 230.5 | 20076 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 44.2 | 100.0 | 165.1 | 238.9 | 20532 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
