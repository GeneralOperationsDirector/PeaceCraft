from textblob import TextBlob


# Define trust thresholds
TRUST_MIN = 0
TRUST_MAX = 100


def analyze_sentiment(text: str) -> float:
    """Analyze sentiment polarity of a player's input.
    Returns value between -1.0 (very negative) and 1.0 (very positive)."""
    return TextBlob(text).sentiment.polarity


def adjust_trust_level(current_trust: int, sentiment_score: float, npc_personality: str) -> int:
    """Adjust trust level based on sentiment and NPC personality."""
    adjustment = 0

    if sentiment_score > 0.2:
        adjustment = 7 if npc_personality.lower() == "emotional" else 5
    elif sentiment_score < -0.2:
        adjustment = -7 if npc_personality.lower() == "aggressive" else -5

    new_trust = current_trust + adjustment
    return max(TRUST_MIN, min(TRUST_MAX, new_trust))
