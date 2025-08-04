import requests
from config import OLLAMA_URL, OLLAMA_MODEL


def call_ollama_model(prompt, model=OLLAMA_MODEL):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.RequestException as e:
        return f"[Error calling Ollama model: {str(e)}]"
