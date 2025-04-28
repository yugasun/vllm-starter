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
	# @echo "To stop the server, run: make stop"

pid:
	@echo "Getting VLLM server PID..."
	@pid=$$(pgrep -f "uv run -m vllm_starter.server") && \
	if [ -z "$$pid" ]; then \
		echo "VLLM server is not running."; \
	else \
		echo "VLLM server PID: $$pid"; \
	fi
	@echo "To stop the server, run: make stop"
	@echo "To check the logs, run: tail -f run.log"

stop:
	@echo "Stopping VLLM server..."
	@pid=$$(pgrep -f "uv run -m vllm_starter.server") && \
	if [ -z "$$pid" ]; then \
		echo "VLLM server is not running."; \
	else \
		pkill -TERM -P $$pid || true && \
		echo "VLLM server stopped."; \
	fi

log:
	@echo "Checking VLLM server logs..."
	@tail -f run.log


test:
	@echo "Running tests..."
	@uv run -m vllm_starter.test
	@echo "Tests completed."
	@echo "To check the logs, run: tail -f run.log"