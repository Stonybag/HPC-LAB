# HPC Lab — Apptainer Container Environment

Hands-on HPC portfolio project: building and running GPU-accelerated containers on Rocky Linux 9.

## What's in this repo
- `hpc_pytorch.def` — Apptainer definition file for a custom PyTorch container
- `matrix_benchmark.py` — CPU/GPU matrix multiply benchmark (GFLOPS output)
- `docs/as-built.md` — As-built documentation and performance results

## Environment
- OS: Rocky Linux 9.8 (RHEL-compatible)
- Container runtime: Apptainer 1.5.2
- Base image: pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime
- Added packages: numpy, scipy, matplotlib, pandas

## Benchmark Results (CPU baseline)
| Matrix Size | Time | GFLOPS |
|-------------|------|--------|
| 1024x1024 | 45.9 ms | 46.8 |
| 2048x2048 | 225.3 ms | 76.3 |
| 4096x4096 | 1669.8 ms | 82.3 |

GPU node with NVIDIA A100 expected to deliver 300,000+ GFLOPS.
