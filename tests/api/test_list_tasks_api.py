from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_list_tasks_returns_list_of_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0
