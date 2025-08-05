# trust.py
from config import TRUST_WIN_THRESHOLD, TRUST_LOSS_THRESHOLD
from database import log_trust_adjustment
from textblob import TextBlob
import os

USE_MEDIATOR = os.getenv("USE_TRUST_MEDIATOR", "false").lower() == "true"

# ---- Sentiment-based trust (fallback) ----
def analyze_sentiment(text):
    """Returns a sentiment polarity score between -1.0 and 1.0"""
    return TextBlob(text).sentiment.polarity

def sentiment_based_trust_adjustment(current_trust, player_input):
    """Adjusts trust based on simple sentiment analysis"""
    sentiment = analyze_sentiment(player_input)
    
    if sentiment > 0.3:
        change = 5
    elif sentiment < -0.3:
        change = -10
    else:
        change = -2

    new_trust = max(0, min(100, current_trust + change))
    return new_trust, change, f"Sentiment score: {sentiment:.2f} → Change: {change}"


# ---- Mediator-based trust adjustment (LLM via Ollama) ----
def mediator_based_trust_adjustment(current_trust, npc_type, conversation_history):
    from ollama import call_ollama_model  # local Ollama call
    from summarization import summarize_conversation

    recent_dialogue = conversation_history[-4:]

    prompt = {
        "system": "You are a trust mediator evaluating a conversation between a player and an NPC. Determine how the player's actions affected trust.",
        "user": f"NPC Type: {npc_type}\nTrust Before: {current_trust}\nRecent Dialogue:\n" +
                "\n".join([f"{msg['role']}: {msg['text']}" for msg in recent_dialogue])
    }

    result = call_ollama_model(prompt)  # You can implement this
    # Expected result format: { "trust_change": -5, "summary": "Player became aggressive..." }

    trust_change = result.get("trust_change", 0)
    summary = result.get("summary", "LLM provided no summary.")
    new_trust = max(0, min(100, current_trust + trust_change))

    return new_trust, trust_change, summary


# ---- Public function to call from main.py ----
def analyze_trust_shift(session_id, npc_type, trust_before, conversation_history):
    """
    Determines trust change based on player input.
    Uses either sentiment model or Ollama mediator depending on config.
    Logs trust event.
    """
    if USE_MEDIATOR:
        trust_after, change, summary = mediator_based_trust_adjustment(
            trust_before, npc_type, conversation_history
        )
    else:
        # Get last player message
        player_input = next((msg["text"] for msg in reversed(conversation_history) if msg["role"] == "player"), "")
        trust_after, change, summary = sentiment_based_trust_adjustment(trust_before, player_input)

    log_trust_adjustment(session_id, npc_type, trust_before, trust_after, summary)
    return trust_after
