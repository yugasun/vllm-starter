.PHONY: all check-cuda install run

run_cmd = "uv run -m vllm_starter.server"

# Verify CUDA is available
check-cuda:
	@echo "Checking CUDA availability..."
	@uv run -m vllm_starter.check_cuda

install:
	uv sync

dev:
	@sh -c ${run_cmd}


run:
	@nohup sh -c ${run_cmd} > /dev/null 2>&1 &
	@echo $$(ps -ef | grep "${run_cmd}" | grep -v grep | awk '{print $$2}') > run.pid
	@echo "VLLM server started. Check run.log for details."
	@echo "To stop the server, run: make stop"

pid:
	@echo "Getting VLLM server PID..."
	@echo $$(ps -ef | grep "${run_cmd}" | grep "vllm-starter/.venv/bin/python" | grep -v grep | awk '{print $$2}') > run.pid
	@echo "VLLM server PID saved to run.pid."
	@echo "To stop the server, run: make stop"
	@echo "To check the logs, run: tail -f run.log"

stop:
	@echo "Stopping VLLM server..."
	@cat run.pid | xargs -n1 sh -c 'pkill -TERM -P $$0 || true && kill -9 $$0 || true'
	@echo "VLLM server stopped."

log:
	@echo "Checking VLLM server logs..."
	@tail -f run.log


test:
	@echo "Running tests..."
	@uv run -m vllm_starter.test
	@echo "Tests completed."
	@echo "To check the logs, run: tail -f run.log"