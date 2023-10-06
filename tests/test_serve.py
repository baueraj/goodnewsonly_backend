import pytest
from fastapi.testclient import TestClient

from goodnewsonly.serve import app

client = TestClient(app)


def test_analyze_endpoint():
    response = client.post("/analyze", json={"url": "https://www.example.com"})
    assert response.status_code == 200
    # You can further check the structure of the response, etc.
