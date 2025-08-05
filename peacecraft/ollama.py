# ollama.py

import requests
import json
from config import OLLAMA_URL, OLLAMA_MODEL


def call_ollama_model(prompt, model=OLLAMA_MODEL):
    """
    Calls the Ollama model with a raw string prompt.
    Returns plain string response.
    """
    payload = {
        "model": model,
        "prompt": json.dumps(prompt) if isinstance(prompt, dict) else prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        raw = response.json()["response"]

        # Attempt to parse LLM response as JSON
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {
                "trust_change": 0,
                "summary": f"Failed to parse JSON. Raw response: {raw[:100]}..."
            }

    except requests.RequestException as e:
        return {
            "trust_change": 0,
            "summary": f"[Ollama error: {str(e)}]"
        }


def call_trust_mediator(system_prompt, user_prompt, model=OLLAMA_MODEL):
    """
    Calls the Ollama model with a system+user prompt for trust mediation.
    Returns a structured result like:
    {
        "trust_change": -5,
        "summary": "Player became aggressive..."
    }
    """
    chat_payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL.replace("/generate", "/chat"), json=chat_payload)
        response.raise_for_status()
        raw_response = response.json().get("message", {}).get("content", "")
        
        # Try to parse response as JSON
        try:
            return json.loads(raw_response)
        except json.JSONDecodeError:
            # Fallback heuristic: wrap response if needed
            return {
                "trust_change": 0,
                "summary": raw_response.strip()
            }
    except requests.RequestException as e:
        return {
            "trust_change": 0,
            "summary": f"[Ollama error: {str(e)}]"
        }
