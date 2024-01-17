from typing import List
from .headline_extractor import extract_headlines
from .sentiment_analysis import SentimentModel

# Initialize with your Hugging Face model name and API token
analyzer = SentimentModel("your_username/distilbert-base-uncased-finetuned-sst-2-english-sentiment-int8", "your_huggingface_api_token")


async def process_website(url: str) -> List[str]:
    headlines = extract_headlines(url)
    # TODO: Remove below print statement =========================================================
    print(headlines)
    sentiments = await analyzer.predict(headlines)
    negative_headlines = [headline for headline, sentiment in zip(headlines, sentiments) if sentiment == "negative"]
    return negative_headlines
