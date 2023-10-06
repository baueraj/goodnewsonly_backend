from goodnewsonly.headline_extractor import extract_headlines


def test_cnn_extraction() -> None:
    # Mock URL for CNN
    headlines = extract_headlines("https://www.cnn.com")
    assert isinstance(headlines, list)
    # You can add more specific tests if you have mock data or expected headlines.


def test_foxnews_extraction() -> None:
    headlines = extract_headlines("https://www.foxnews.com")
    assert isinstance(headlines, list)


def test_bbc_extraction() -> None:
    headlines = extract_headlines("https://www.bbc.com/news")
    assert isinstance(headlines, list)
