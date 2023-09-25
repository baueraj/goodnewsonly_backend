# headline_extractor.py

import requests
from bs4 import BeautifulSoup
from typing import List

class BaseNewsDomain:
    def __init__(self, url: str):
        self.url = url

    def _get_page_content(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, 'html.parser')

    def extract_headlines(self) -> List[str]:
        raise NotImplementedError("This method should be overridden by subclasses.")

class CNNNewsDomain(BaseNewsDomain):
    def extract_headlines(self) -> List[str]:
        soup = self._get_page_content()
        headlines = soup.find_all('h3', class_='cd__headline')
        return [headline.text for headline in headlines]

class FoxNewsDomain(BaseNewsDomain):
    def extract_headlines(self) -> List[str]:
        soup = self._get_page_content()
        headlines = soup.find_all('h2', class_='title')
        return [headline.text for headline in headlines]

class BBCNewsDomain(BaseNewsDomain):
    def extract_headlines(self) -> List[str]:
        soup = self._get_page_content()
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        return [headline.text for headline in headlines]

def extract_from_known_domain(url: str) -> List[str]:
    if "cnn.com" in url:
        return CNNNewsDomain(url).extract_headlines()
    elif "foxnews.com" in url:
        return FoxNewsDomain(url).extract_headlines()
    elif "bbc.com/news" in url:
        return BBCNewsDomain(url).extract_headlines()
    else:
        return []

class DOMParser:
    def __init__(self, html: str):
        self.html = html

    def extract_headlines(self) -> List[str]:
        soup = BeautifulSoup(self.html, 'html.parser')
        headlines = soup.find_all('h1')
        return [headline.text for headline in headlines]

def extract_from_general_domain(html: str) -> List[str]:
    parser = DOMParser(html)
    return parser.extract_headlines()

def extract_headlines(url: str) -> List[str]:
    headlines = extract_from_known_domain(url)
    if not headlines:
        html = requests.get(url).text
        headlines = extract_from_general_domain(html)
    return headlines
