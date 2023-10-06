from typing import Dict

from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, headline: str) -> str:
        sentiment_scores = self.sia.polarity_scores(headline)
        if sentiment_scores["compound"] >= 0.05:
            return "positive"
        elif sentiment_scores["compound"] <= -0.05:
            return "negative"
        else:
            return "neutral"
