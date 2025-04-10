.PHONY: all check-cuda install run

# Verify CUDA is available
check-cuda:
	@echo "Checking CUDA availability..."
	@uv run -m vllm_starter.check_cuda

install:
	uv sync

dev:
	@uv run -m vllm_starter.server


run:
	@uv run -m vllm_starter.server > run.log 2>&1 &
	@echo "VLLM server started. Check run.log for details."
