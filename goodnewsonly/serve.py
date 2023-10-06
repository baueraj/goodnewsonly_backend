import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api_models import AnalysisRequest
from .core import process_website

#
# HOSTNAME = os.environ.get("HOSTNAME", "unknown")
#
# log_level = os.getenv("LOG_LEVEL", default="info")
# log_level_map = {
#     "debug": logging.DEBUG,
#     "info": logging.INFO,
#     "warning": logging.WARNING,
#     "error": logging.ERROR,
# }
# print(f"Setting log level to {log_level}")
# LOGGING_FORMAT = "[%(asctime)s.%(msecs)03d][%(levelname)s ][%(module)s.%(funcName)s ][%(threadName)s ] - %(message)s"
# logging.basicConfig(format=LOGGING_FORMAT, level=log_level_map[log_level], datefmt="%Y-%m-%d %H:%M:%S")
# logger = logging.getLogger(__name__)

app = FastAPI(title="GoodNewsOnly")

# CORS middleware settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    negative_headlines = process_website(request.url)
    return {"headlines": negative_headlines}
