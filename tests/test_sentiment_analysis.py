import pytest

from goodnewsonly.sentiment_analysis import SentimentAnalyzer


def test_positive_sentiment():
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("This is a great day!")
    assert sentiment == "positive"


def test_negative_sentiment():
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("This is a terrible mistake.")
    assert sentiment == "negative"


def test_neutral_sentiment():
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("The sky is blue.")
    assert sentiment == "neutral"
