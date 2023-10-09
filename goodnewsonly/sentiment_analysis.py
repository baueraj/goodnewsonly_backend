import gzip
import io
import os
from typing import List

import torch
from transformers import DistilBertTokenizer

pretrained_model_name = "distilbert-base-uncased-finetuned-sst-2-english"

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "resources", "quant_model_weights_and_arch.pth.gz")


class SentimentAnalyzer:
    def __init__(self) -> None:
        self.tokenizer = DistilBertTokenizer.from_pretrained(pretrained_model_name)
        with gzip.open(model_path, "rb") as f:
            buffer = f.read()
        self.model = torch.load(io.BytesIO(buffer))

    def analyze_sentiments(self, headlines: List[str]) -> List[str]:
        inputs = self.tokenizer(headlines, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        pred_class_ids = logits.argmax(dim=1).tolist()
        pred_class_labels = [self.model.config.id2label[id_].strip().lower() for id_ in pred_class_ids]
        return pred_class_labels
