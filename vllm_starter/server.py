import os
from vllm_starter.config import settings, config_path
import torch
from vllm_starter.logger import setup_logger
import subprocess

logger = setup_logger()


logger.info("Checking CUDA availability...")
logger.info("CUDA device count:", torch.cuda.device_count())

is_cuda_available = torch.cuda.is_available()

if is_cuda_available:
    logger.info("CUDA device name:", torch.cuda.get_device_name(0))
else:
    logger.info("CUDA is not available. Please check your installation.")
    raise RuntimeError("CUDA is not available. Please check your installation.")

# Reset CUDA before starting server
torch.cuda.empty_cache()


def main():
    port = int(settings.get("port", 8000))
    host = settings.get("host", "127.0.0.1")
    model = settings.get("model", "facebook/opt-125m")

    # Start the server
    logger.info(f"Starting vLLM server with model: {model}")

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
    logger.info(f"Server arguments: {args}")

    # run shell command, parse args to `vllm serve` comman
    cmd = f"vllm serve {model} --port {port} --host {host} {args}"

    logger.info(f"Command: {cmd}")

    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1,
    )

    for line in process.stdout:
        logger.info(line.rstrip())

    process.stdout.close()
    return_code = process.wait()
    if return_code != 0:
        logger.error(f"Server exited with code {return_code}")


def run():
    # This function is not used in the current script but can be useful for testing
    # or running the server in a different context.
    main()


if __name__ == "__main__":
    main()
