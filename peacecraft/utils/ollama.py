import requests
from peacecraft.config import OLLAMA_URL, OLLAMA_MODEL


def generate_response(prompt: str, model: str = OLLAMA_MODEL) -> str:
    """Send a prompt to the Ollama API and return the response."""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.RequestException as e:
        print(f"⚠️ Ollama request failed: {e}")
        return "[Error connecting to LLM]"
