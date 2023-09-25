from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api_models import AnalysisRequest
from .core import process_website


app = FastAPI()

# CORS middleware settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    negative_headlines = process_website(request.url)
    return {"headlines": negative_headlines}
