# peacecraft/services/ollama_client.py

import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral-nemo"


def send_prompt_to_ollama(prompt: str, stream: bool = True) -> str:
    """Send prompt to Ollama model and return full response."""
    headers = {"Content-Type": "application/json"}
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": stream}

    response = requests.post(
        OLLAMA_API_URL, headers=headers, json=payload, stream=stream
    )

    if not response.ok:
        raise RuntimeError(
            f"Ollama request failed: {response.status_code} - {response.text}"
        )

    output = ""
    try:
        for line in response.iter_lines(decode_unicode=True):
            if line.strip():
                data = json.loads(line)
                if "response" in data:
                    output += data["response"]
    except Exception as e:
        raise RuntimeError(f"Error streaming Ollama response: {str(e)}")

    return output.strip()
