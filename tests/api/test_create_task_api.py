from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_task_api_creates_task_and_returns_json():
    payload = {"title": "API task", "description": "Created via API"}

    response = client.post("/tasks", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["is_completed"] is False
    assert data["id"] is not None
