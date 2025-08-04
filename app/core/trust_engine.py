# peacecraft/core/trust_engine.py

import re
from textblob import TextBlob
from peacecraft.core.npc_profiles import get_npc_profile


def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Range: -1 (negative) to +1 (positive)


def match_traits(text, traits):
    matches = 0
    for phrase in traits.lower().split("."):
        if phrase.strip() and re.search(re.escape(phrase.strip()), text.lower()):
            matches += 1
    return matches


def score_clarity(text):
    word_count = len(text.split())
    if word_count >= 12:
        return 1  # Bonus for thorough response
    elif word_count <= 3:
        return -1  # Penalize overly short response
    return 0


def calculate_trust_change(npc_personality, player_response):
    profile = get_npc_profile(npc_personality)
    sentiment_score = analyze_sentiment(player_response)
    win_match = match_traits(player_response, profile.get("how_to_win", ""))
    lose_match = match_traits(player_response, profile.get("how_to_lose", ""))
    clarity_bonus = score_clarity(player_response)

    # Weighted score components
    sentiment_weight = sentiment_score * 10  # Range ~ -10 to +10
    win_weight = win_match * 5
    lose_weight = lose_match * -5
    clarity_weight = clarity_bonus * 2

    total_score = sentiment_weight + win_weight + lose_weight + clarity_weight
    return int(max(min(total_score, 15), -15))  # Clamp between -15 and +15
