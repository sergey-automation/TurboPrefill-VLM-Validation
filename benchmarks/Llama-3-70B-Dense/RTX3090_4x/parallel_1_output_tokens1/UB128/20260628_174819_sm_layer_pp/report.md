# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `1`
- BATCH: `16384`
- UBATCH: `128`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_174819/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 254 | 0.58 | 441.12 |
| ctx_000512.txt | 1 | 510 | 1.17 | 435.31 |
| ctx_001024.txt | 1 | 1022 | 2.34 | 436.19 |
| ctx_002048.txt | 1 | 2046 | 4.72 | 433.43 |
| ctx_004096.txt | 1 | 4094 | 9.65 | 424.31 |
| ctx_008192.txt | 1 | 8190 | 20.19 | 405.63 |
| ctx_016384.txt | 1 | 16382 | 43.83 | 373.79 |
| ctx_032768.txt | 1 | 32767 | 102.01 | 321.22 |
| ctx_065536.txt | 1 | 65534 | 261.19 | 250.90 |
| ctx_100000.txt | 1 | 99998 | 494.51 | 202.22 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 444.23 | 0.57 | 0.58 |
| ctx_000512.txt | 1 | 1 | 510 | 475.29 | 1.07 | 1.17 |
| ctx_001024.txt | 1 | 1 | 1022 | 475.65 | 2.15 | 2.34 |
| ctx_002048.txt | 1 | 1 | 2046 | 470.38 | 4.35 | 4.72 |
| ctx_004096.txt | 1 | 1 | 4094 | 458.71 | 8.93 | 9.65 |
| ctx_008192.txt | 1 | 1 | 8190 | 436.52 | 18.76 | 20.19 |
| ctx_016384.txt | 1 | 1 | 16382 | 399.48 | 41.01 | 43.83 |
| ctx_032768.txt | 1 | 1 | 32767 | 341.14 | 96.05 | 102.01 |
| ctx_065536.txt | 1 | 1 | 65534 | 263.31 | 248.88 | 261.19 |
| ctx_100000.txt | 1 | 1 | 99998 | 212.43 | 470.72 | 494.50 |

## GPU load during group response window

### ctx_000256.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 1.0 | 1.0 | 105.6 | 105.6 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 121.7 | 121.7 | 19330 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.5 | 109.5 | 19330 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 112.1 | 112.1 | 19698 |

### ctx_000512.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 112.0 | 112.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 128.6 | 128.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.9 | 116.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 118.7 | 118.7 | 19706 |

### ctx_001024.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 21.0 | 42.0 | 109.8 | 123.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.5 | 67.0 | 129.1 | 138.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 12.5 | 25.0 | 115.2 | 122.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.7 | 123.3 | 19706 |

### ctx_002048.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.2 | 62.0 | 121.2 | 131.6 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.8 | 62.0 | 139.7 | 150.0 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.8 | 67.0 | 126.5 | 136.0 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 13.4 | 55.0 | 128.8 | 137.7 | 19706 |

### ctx_004096.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 27.2 | 64.0 | 123.5 | 130.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 19.1 | 70.0 | 142.4 | 149.4 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 4.6 | 36.0 | 130.1 | 137.5 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.9 | 51.0 | 131.4 | 138.5 | 19706 |

### ctx_008192.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 26.9 | 69.0 | 125.7 | 132.6 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.6 | 78.0 | 146.5 | 155.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.6 | 73.0 | 131.2 | 140.2 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 13.9 | 67.0 | 131.9 | 138.8 | 19706 |

### ctx_016384.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 22.7 | 78.0 | 125.7 | 134.8 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.4 | 85.0 | 147.6 | 157.2 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.5 | 80.0 | 132.8 | 140.5 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.9 | 79.0 | 133.0 | 141.6 | 19706 |

### ctx_032768.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 25.3 | 100.0 | 126.3 | 134.5 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 30.4 | 100.0 | 145.9 | 156.0 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.7 | 100.0 | 132.6 | 144.2 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 18.7 | 100.0 | 132.4 | 142.4 | 19706 |

### ctx_065536.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 21.4 | 100.0 | 126.0 | 136.8 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.1 | 100.0 | 145.7 | 157.3 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.8 | 100.0 | 133.7 | 150.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.9 | 100.0 | 132.8 | 143.7 | 19706 |

### ctx_100000.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 23.6 | 100.0 | 126.1 | 147.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.9 | 100.0 | 145.1 | 166.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.7 | 100.0 | 132.8 | 154.3 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.4 | 100.0 | 132.2 | 153.0 | 19706 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
