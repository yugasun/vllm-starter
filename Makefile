.PHONY: all check-cuda install run

# Verify CUDA is available
check-cuda:
	@echo "Checking CUDA availability..."
	python3 -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('CUDA device count:', torch.cuda.device_count()); print('Current CUDA device:', torch.cuda.current_device())"

install:
	uv sync

# Add CUDA initialization and clean GPU memory before running
run:
	@uv run -m vllm_starter.server > run.log 2>&1 &
	@echo "VLLM server started. Check run.log for details."
