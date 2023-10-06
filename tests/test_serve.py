from fastapi.testclient import TestClient

from goodnewsonly.serve import app

client = TestClient(app)


def test_analyze_endpoint() -> None:
    # TODO: Add more checks of the response
    response = client.post("/analyze", json={"url": "https://www.example.com"})
    assert response.status_code == 200
