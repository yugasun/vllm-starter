FROM vllm/vllm-openai:latest

# e.g. install the `audio` optional dependencies
# NOTE: Make sure the version of vLLM matches the base image!
# RUN uv pip install --system vllm[audio]==0.8.3

ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server"]