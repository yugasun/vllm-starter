# change to the version you want to use
FROM vllm/vllm-openai:v0.8.5

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/

# maintainer
LABEL maintainer="Yuga Sun <yugasun.ai@gmail.com>"
# e.g. install the `audio` optional dependencies
# NOTE: Make sure the version of vLLM matches the base image!
# RUN uv pip install --system vllm[audio]==0.8.3

ADD . .
RUN uv sync --no-cache-dir

ENTRYPOINT ["uv", "run", "-m", "vllm_starter.server"]