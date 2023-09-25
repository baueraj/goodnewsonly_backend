# core.py

from .headline_extractor import extract_headlines
from .sentiment_analysis import SentimentAnalyzer

def process_website(url: str):
    """Process the given website URL to extract and analyze headlines."""
    headlines = extract_headlines(url)
    negative_headlines = []
    analyzer = SentimentAnalyzer()

    for headline in headlines:
        sentiment = analyzer.analyze_sentiment(headline)
        if sentiment == "negative":
            negative_headlines.append(headline)

    return negative_headlines
