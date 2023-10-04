from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    url: str
