# import logging
# import os

from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api_models import AnalysisRequest
from .core import process_website

app = FastAPI(title="GoodNewsOnly")

# CORS middleware settings
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# TODO: Remove "all" permissions later for security purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello, world!"}


@app.post("/analyze")
async def analyze(request: AnalysisRequest) -> Dict[str, Any]:
    negative_headlines = process_website(request.url)
    return {"headlines": negative_headlines}
