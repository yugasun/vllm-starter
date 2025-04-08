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
sudo systemctl enable nvidia-fabricmanager
sudo systemctl start nvidia-fabricmanager
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

## Development

```bash
make dev
```

This will start a development server.

## Specify the CUDA available devices
You can specify the CUDA devices available to the vLLM server by setting the `CUDA_VISIBLE_DEVICES` environment variable. For example, to make only GPU 0 and GPU 1 available, you can run:

```bash
export CUDA_VISIBLE_DEVICES=0,1
```

This will limit the vLLM server to use only GPU 0 and GPU 1. You can also set this variable in your `config.yaml` file under the `cuda_visible_devices` key.

## Use ModelScope models

The vLLM use HuggingFace models by default. To use [ModelScope](https://www.modelscope.cn/) models, you need to set environment variable `VLLM_USE_MODELSCOPE` to `True`.

```bash
export VLLM_USE_MODELSCOPE=True
```

Then, you can use ModelScope models in your vLLM server. For example, to use the `llama-2-7b-chat` model from ModelScope, you can run:

```bash
from vllm import LLM

llm = LLM(model="Qwen1.5-0.5B-Chat", trust_remote_code=True)

# For generative models (task=generate) only
output = llm.generate("Hello, my name is")
print(output)
```

## License

[Apache License 2.0](./LICENSE)