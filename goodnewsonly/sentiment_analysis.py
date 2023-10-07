import os

from nltk.sentiment import SentimentIntensityAnalyzer

current_dir = os.path.dirname(os.path.abspath(__file__))
lexicon_file_path = os.path.join(current_dir, "resources", "vader_lexicon.txt")


class SentimentAnalyzer:
    def __init__(self) -> None:
        self.sia = SentimentIntensityAnalyzer(lexicon_file=lexicon_file_path)

    def analyze_sentiment(self, headline: str) -> str:
        sentiment_scores = self.sia.polarity_scores(headline)
        if sentiment_scores["compound"] >= 0.05:
            return "positive"
        elif sentiment_scores["compound"] <= -0.05:
            return "negative"
        else:
            return "neutral"
