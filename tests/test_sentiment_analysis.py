from goodnewsonly.sentiment_analysis import SentimentAnalyzer


def test_positive_sentiment() -> None:
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiments(["This is a great day!"])[0]
    assert sentiment == "positive"


def test_negative_sentiment() -> None:
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiments(["This is a terrible mistake"])[0]
    assert sentiment == "negative"
