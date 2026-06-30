# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `1`
- BATCH: `16384`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `tensor`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_171539/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 1 -ctk f16 -sm tensor -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 254 | 0.50 | 508.21 |
| ctx_000512.txt | 1 | 510 | 1.10 | 463.26 |
| ctx_001024.txt | 1 | 1022 | 1.95 | 524.56 |
| ctx_002048.txt | 1 | 2046 | 3.55 | 576.44 |
| ctx_004096.txt | 1 | 4094 | 7.25 | 564.89 |
| ctx_008192.txt | 1 | 8190 | 14.41 | 568.53 |
| ctx_016384.txt | 1 | 16382 | 29.48 | 555.61 |
| ctx_032768.txt | 1 | 32767 | 63.29 | 517.75 |
| ctx_065536.txt | 1 | 65534 | 144.53 | 453.44 |
| ctx_100000.txt | 1 | 99998 | 255.61 | 391.22 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 512.36 | 0.50 | 0.50 |
| ctx_000512.txt | 1 | 1 | 510 | 536.01 | 0.95 | 1.10 |
| ctx_001024.txt | 1 | 1 | 1022 | 616.51 | 1.66 | 1.95 |
| ctx_002048.txt | 1 | 1 | 2046 | 685.88 | 2.98 | 3.55 |
| ctx_004096.txt | 1 | 1 | 4094 | 666.63 | 6.14 | 7.25 |
| ctx_008192.txt | 1 | 1 | 8190 | 667.66 | 12.27 | 14.40 |
| ctx_016384.txt | 1 | 1 | 16382 | 647.96 | 25.28 | 29.48 |
| ctx_032768.txt | 1 | 1 | 32767 | 600.32 | 54.58 | 63.29 |
| ctx_065536.txt | 1 | 1 | 65534 | 516.80 | 126.81 | 144.52 |
| ctx_100000.txt | 1 | 1 | 99998 | 452.57 | 220.95 | 255.60 |

## GPU load during group response window

### ctx_000256.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 101.6 | 101.6 | 14854 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 1.0 | 1.0 | 118.4 | 118.4 | 21342 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 1.0 | 1.0 | 108.2 | 108.2 | 21342 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 1.0 | 1.0 | 109.2 | 109.2 | 21342 |

### ctx_000512.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 112.3 | 112.3 | 14854 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 129.4 | 129.4 | 21342 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 118.2 | 118.2 | 21342 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 117.7 | 117.7 | 21342 |

### ctx_001024.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 67.5 | 100.0 | 129.3 | 133.7 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 62.5 | 100.0 | 148.3 | 150.8 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 51.5 | 100.0 | 143.4 | 145.4 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 142.3 | 143.2 | 21398 |

### ctx_002048.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 66.7 | 100.0 | 132.4 | 147.1 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 154.3 | 172.4 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 145.6 | 162.7 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 66.7 | 100.0 | 147.4 | 166.6 | 21398 |

### ctx_004096.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 70.3 | 100.0 | 132.4 | 148.4 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 68.1 | 100.0 | 155.6 | 178.0 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 67.3 | 100.0 | 145.8 | 167.2 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 67.3 | 100.0 | 149.5 | 172.2 | 21398 |

### ctx_008192.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 75.2 | 100.0 | 137.0 | 149.6 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 75.2 | 100.0 | 162.7 | 180.2 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 76.5 | 100.0 | 151.3 | 168.4 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 76.9 | 100.0 | 155.4 | 173.6 | 21398 |

### ctx_016384.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 83.2 | 100.0 | 140.3 | 151.1 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 81.7 | 100.0 | 170.5 | 188.1 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 82.4 | 100.0 | 156.3 | 171.4 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.5 | 100.0 | 159.1 | 173.1 | 21398 |

### ctx_032768.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.6 | 100.0 | 142.0 | 153.0 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.2 | 100.0 | 176.0 | 194.4 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.6 | 100.0 | 160.6 | 178.5 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.6 | 100.0 | 162.6 | 180.1 | 21398 |

### ctx_065536.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 85.9 | 100.0 | 144.7 | 156.3 | 14910 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.9 | 100.0 | 182.0 | 206.5 | 21398 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.7 | 100.0 | 166.0 | 188.2 | 21398 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 84.8 | 100.0 | 167.7 | 189.4 | 21398 |

### ctx_100000.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 84.4 | 100.0 | 144.4 | 164.6 | 14912 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.6 | 100.0 | 184.2 | 219.9 | 21400 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.3 | 100.0 | 168.4 | 204.4 | 21400 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 83.0 | 100.0 | 170.1 | 205.9 | 21400 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
