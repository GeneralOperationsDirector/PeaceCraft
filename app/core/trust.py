# peacecraft/core/trust.py

from textblob import TextBlob


def analyze_sentiment(text: str) -> float:
    """
    Analyze sentiment polarity of a player's input.
    Returns value in range [-1.0, 1.0] where 0 is neutral.
    """
    return TextBlob(text).sentiment.polarity


def update_trust_level(current_trust: int, sentiment_score: float) -> int:
    """
    Adjust trust level based on sentiment score.
    Sentiment > 0 increases trust, < 0 decreases it.
    """
    adjustment = int(sentiment_score * 10)
    new_trust = max(0, min(100, current_trust + adjustment))
    return new_trust
