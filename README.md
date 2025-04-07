# vLLM Starter

Use this template to kickstart your vLLM project.


## Prerequisites

- Ubuntu 22.04
- Python 3.12+
- uv 0.5.8+

CUDA Toolkit 12.4 is required for GPU support. You can install it using the following command:

```bash
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda_12.4.0_550.54.14_linux.run
sudo sh cuda_12.4.0_550.54.14_linux.run
sudo reboot
```

Install Nvidia Fabric Manager and the driver using the following command:

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/nvidia-fabricmanager-550_550.54.14-1_amd64.deb
sudo dpkg -i nvidia-fabricmanager-550_550.54.14-1_amd64.deb
```

## Installation

```bash
make install
```

## Usage

1. Configure for the vLLM server. Please copy the `config.example.yaml` file to `config.yaml` and modify it according to your needs.


2. Start the vLLM server:

```bash
make run
```

## License

MIT License