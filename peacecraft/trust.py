from textblob import TextBlob
from config import TRUST_WIN_THRESHOLD, TRUST_LOSS_THRESHOLD

def analyze_sentiment(text):
    """Returns a sentiment polarity score between -1.0 and 1.0"""
    return TextBlob(text).sentiment.polarity

def adjust_trust_level(current_trust, player_input):
    """Adjusts trust level based on sentiment of player input"""
    sentiment = analyze_sentiment(player_input)
    
    # Positive sentiment → increase trust
    if sentiment > 0.3:
        change = 5
    # Negative sentiment → decrease trust
    elif sentiment < -0.3:
        change = -10
    # Neutral → slight trust drop
    else:
        change = -2

    new_trust = max(0, min(100, current_trust + change))
    return new_trust
