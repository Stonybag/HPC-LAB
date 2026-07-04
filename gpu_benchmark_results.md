# Project 3: Multi-GPU Benchmark Results

## Environment
- Cloud: Vast.ai | Instance: 43848821 | Virginia US
- GPU: 2x NVIDIA GeForce RTX 5090 (32607 MiB each)
- Driver: 580.159.03 | CUDA: 13.0
- PyTorch: 2.12.0.dev20260408+cu128 | NCCL: 2.29.7
- CPU: AMD EPYC 7B12 | RAM: 120.9 GB | OS: Ubuntu 24.04.4 LTS

## NCCL All-Reduce (Inter-GPU Bandwidth)
| Size   | Time (ms) | Bandwidth (GB/s) |
|--------|-----------|------------------|
| 1 MB   | 0.186     | 11.25            |
| 4 MB   | 0.593     | 14.14            |
| 16 MB  | 2.156     | 15.57            |
| 64 MB  | 8.620     | 15.57            |
| 256 MB | 34.623    | 15.51            |
Peak: 15.57 GB/s (PCIe 4.0 x16 — no NVLink on RTX consumer cards)

## STREAM Memory Bandwidth
| Function | Bandwidth (MB/s) |
|----------|-----------------|
| Copy     | 30,516.7        |
| Scale    | 21,342.7        |
| Add      | 24,246.8        |
| Triad    | 24,552.7        |
Triad: 24.55 GB/s (system memory bandwidth)

## PyTorch GEMM (GPU FLOPS)
- GPU 0: 216.48 TFLOPS FP16
- Theoretical peak: 215.2 TFLOPS (100.6% efficiency)

## NVIDIA DCGM GPU Monitoring (during GEMM load)
| Metric      | Idle  | Under Load |
|-------------|-------|------------|
| SM Clock    | 180 MHz | 2,752 MHz  |
| Temperature | 28°C  | 48°C       |
| Power       | 20W   | 545W       |
| Fan Speed   | 0%    | 30%        |
DCGM version: 3.3.9
