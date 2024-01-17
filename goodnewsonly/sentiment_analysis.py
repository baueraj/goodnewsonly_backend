from typing import List
import httpx
from transformers import DistilBertTokenizer


class SentimentModel:
    def __init__(self, model_name: str, api_token: str) -> None:
        self.model_name = model_name
        self.api_token = api_token
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

    async def predict(self, headlines) -> List[str]:
        inputs = self.tokenizer(headlines, return_tensors="pt", padding=True, truncation=True).data
        # inputs = self.tokenizer(headlines, return_tensors="pt", padding=True, truncation=True)
        # with torch.no_grad():
        #     logits = self.model(**inputs).logits
        # pred_class_ids = logits.argmax(dim=1).tolist()
        # pred_class_labels = [self.model.config.id2label[id_].strip().lower() for id_ in pred_class_ids]
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api-inference.huggingface.co/models/{self.model_name}",
                headers={"Authorization": f"Bearer {self.api_token}"},
                json=inputs
            )
        response_json = response.json()
        # Extract and return predictions from response
        # ...
        return pred_class_labels
