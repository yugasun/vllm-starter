import os
from vllm_starter.config import settings, config_path
import torch

print("Checking CUDA availability...")
print("CUDA device count:", torch.cuda.device_count())

is_cuda_available = torch.cuda.is_available()

if is_cuda_available:
    print("CUDA device name:", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available. Please check your installation.")
    raise RuntimeError("CUDA is not available. Please check your installation.")

# Reset CUDA before starting server
torch.cuda.empty_cache()


def main():
    port = int(settings.get("port", 8000))
    host = settings.get("host", "127.0.0.1")
    model = settings.get("model", "facebook/opt-125m")

    # Start the server
    print(f"Starting vLLM server with model: {model}")

    # add all properties in settings to the command arguments
    args = []
    for key, value in settings.items():
        if key not in ["port", "host", "model"]:
            if isinstance(value, bool):
                if value:
                    args.append(f"--{key}")
            elif isinstance(value, list):
                args.append(f"--{key} {" ".join(value)}")
            else:
                args.append(f"--{key} {value}")
    # add config path to args
    args = " ".join(args)
    print(f"Server arguments: {args}")

    # run shell command, parse args to `vllm serve` comman
    cmd = f"vllm serve {model} --port {port} --host {host} {args}"

    print(f"Command: {cmd}")

    os.system(cmd)


def run():
    # This function is not used in the current script but can be useful for testing
    # or running the server in a different context.
    main()


if __name__ == "__main__":
    main()
