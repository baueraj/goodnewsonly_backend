from goodnewsonly.headline_extractor import extract_headlines


def test_cnn_extraction() -> None:
    headlines = extract_headlines("https://www.cnn.com")
    if True:
        print("\n================================")
        print("~~CNN~~ HEADLINE CANDIDATES")
        print("================================\n")
        print(headlines)
        print(f"\n# of CNN headlines: {len(headlines)}\n\n")
    assert isinstance(headlines, list)


def test_foxnews_extraction() -> None:
    headlines = extract_headlines("https://www.foxnews.com")
    if True:
        print("\n================================")
        print("~~FOX~~ HEADLINE CANDIDATES")
        print("================================\n")
        print(headlines)
        print(f"\n# of Fox headlines: {len(headlines)}\n\n")
    assert isinstance(headlines, list)


def test_bbc_extraction() -> None:
    headlines = extract_headlines("https://www.bbc.com/news")
    if False:
        print("\n================================")
        print("~~BBC~~ HEADLINE CANDIDATES")
        print("================================\n")
        print(headlines)
        print(f"\n# of BBC headlines: {len(headlines)}\n\n")
    assert isinstance(headlines, list)
