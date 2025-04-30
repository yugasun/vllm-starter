# filepath: /data/yugasun/vllm-starter/Dockerfile
# Use a specific version tag for the base image
FROM vllm/vllm-openai:v0.8.5

# Set maintainer label
LABEL maintainer="Yuga Sun <yugasun.ai@gmail.com>"

# Set working directory
WORKDIR /vllm-workspace

# Install dependencies using uv sync for potentially faster installs
# Use --system to install into the system Python environment
# Use --no-cache-dir to avoid caching downloads within the layer, reducing size
RUN uv pip install --system --no-cache-dir loguru==0.7.3 pyyaml==6.0.2 
# Optional: Clean up uv cache if needed, though --no-cache-dir should handle it
# RUN rm -rf /root/.cache/uv

# Copy the rest of the application code
COPY vllm_starter/ ./vllm_starter/

# Set the entrypoint for the container
ENTRYPOINT ["uv", "run", "-m", "vllm_starter.server"]

# Expose the port the application runs on (if applicable, adjust as needed)
EXPOSE 9090