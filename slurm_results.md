# Slurm HPC Cluster — Lab Results

## Cluster Configuration
| Node | Hostname | IP | Role | CPUs | RAM |
|------|----------|----|------|------|-----|
| VM 1 | hpc-node1 | 192.168.197.134 | Head + Compute | 1 vCPU | 7648 MB |
| VM 2 | hpc-node2 | 192.168.197.135 | Compute | 1 vCPU | 3622 MB |
| VM 3 | hpc-node3 | 192.168.197.136 | Compute | 1 vCPU | 3622 MB |

- **OS:** Rocky Linux 9.8
- **Scheduler:** Slurm 25.11.4 (OpenHPC 3)
- **Auth:** Munge 0.5.13
- **MPI:** OpenMPI 4.1.5 (openmpi4-pmix-gnu12-ohpc, PMIx-enabled)
- **Platform:** VMware Workstation Pro 17

## Job Results

### Job 1 — Single-node hostname test

**Result:** PASS — job scheduled and executed on head node.

### Job 6 — Multi-node MPI (3 ranks across 3 nodes)

**Result:** PASS — all 3 MPI ranks executed on separate nodes concurrently.

## Key Configuration Notes
- MpiDefault=pmix in slurm.conf (requires OpenHPC PMIx-enabled OpenMPI)
- Firewall: ports 6817/6818 + full 192.168.197.0/24 subnet accepted
- cgroup.conf: CgroupPlugin=autodetect
- DebugFlags=NO_CONF_HASH (suppresses config hash mismatch warnings across nodes)
