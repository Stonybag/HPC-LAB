# As-Built: Apptainer HPC Container Environment

## Environment
- Host OS: Rocky Linux 9.8 (VMware Workstation Pro 17)
- Apptainer version: 1.5.2-1.el9
- Base image: pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime
- Custom packages added: numpy, scipy, matplotlib, pandas

## Container Build
- Definition file: hpc_pytorch.def
- Output image: hpc_pytorch.sif
- Build command: apptainer build hpc_pytorch.sif hpc_pytorch.def

## Performance Results (CPU baseline — no GPU)
Host: hpc-node1
PyTorch: 2.3.0
CUDA available: False
Running on: cpu

Matrix 1024x1024:  45.9 ms/iter |  46.8 GFLOPS
Matrix 2048x2048: 225.3 ms/iter |  76.3 GFLOPS
Matrix 4096x4096: 1669.8 ms/iter |  82.3 GFLOPS

Note: GPU node with NVIDIA A100 expected to deliver 300,000+ GFLOPS.
Add --nv flag to apptainer exec for CUDA passthrough on real HPC hardware.

## Key Configurations
- No root required to run containers (Apptainer rootless security model)
- GPU passthrough ready: add --nv flag to apptainer exec for CUDA access
- Portable: .sif file transfers to any HPC cluster and runs identically

## Next Steps
- Integrate with Slurm job submissions (Project 4)
- Test GPU acceleration on cloud instance (Project 2/3)
