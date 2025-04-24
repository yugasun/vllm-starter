from openai import OpenAI
import requests
from vllm_starter.config import settings

port = int(settings.get("port", 8000))
host = settings.get("host", "127.0.0.1")

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = settings.get("api-key", "")
openai_api_base = f"http://{host}:{port}/v1"


def get_model_list():
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json",
    }
    res = requests.get(f"{openai_api_base}/models", headers=headers)
    if res.status_code == 200:
        res = res.json()
        if "data" in res:
            return res["data"]
        else:
            raise Exception(f"Invalid response: {res}")
    else:
        raise Exception(f"Failed to get models: {res.status_code} {res.text}")


def run():
    try:
        models = get_model_list()
        model_names = [model["id"] for model in models]
        print(f"Available models: {model_names}")

        first_model_id = models[0]["id"]
        print(f"First model ID: {first_model_id}")

        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )
        completion = client.completions.create(model=first_model_id, prompt="Hello")
        print(f"Completion: {completion}")
        print("vLLM server is running and accessible.")
    except Exception as e:
        print(f"Error: {e}")
        print("Please check if the vLLM server is running and accessible.")


if __name__ == "__main__":
    run()
