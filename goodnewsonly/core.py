from typing import List

from .headline_extractor import extract_headlines
from .sentiment_analysis import SentimentAnalyzer

analyzer = SentimentAnalyzer()


def process_website(url: str) -> List[str]:
    headlines = extract_headlines(url)
    # TODO: Remove below print statement =========================================================
    print(headlines)
    sentiments = analyzer.analyze_sentiments(headlines)
    negative_headlines = [headline for headline, sentiment in zip(headlines, sentiments) if sentiment == "negative"]
    return negative_headlines
