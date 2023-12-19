from goodnewsonly.headline_extractor import extract_headlines


def test_cnn_extraction() -> None:
    headlines = extract_headlines("https://www.cnn.com")
    print(headlines)
    print("\n================================")
    print(len(headlines))
    assert isinstance(headlines, list)


def test_foxnews_extraction() -> None:
    headlines = extract_headlines("https://www.foxnews.com")
    assert isinstance(headlines, list)


def test_bbc_extraction() -> None:
    headlines = extract_headlines("https://www.bbc.com/news")
    assert isinstance(headlines, list)
