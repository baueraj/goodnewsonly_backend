import os

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

current_dir = os.path.dirname(os.path.abspath(__file__))
nltk.data.path.append(os.path.join(current_dir, "resources"))  # Location of vader_lexicon.txt for self.sia


class SentimentAnalyzer:
    def __init__(self) -> None:
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, headline: str) -> str:
        sentiment_scores = self.sia.polarity_scores(headline)
        if sentiment_scores["compound"] >= 0.05:
            return "positive"
        elif sentiment_scores["compound"] <= -0.05:
            return "negative"
        else:
            return "neutral"
