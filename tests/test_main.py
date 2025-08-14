from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_create_item():
    item = {"id": 1, "name": "Test Item", "description": "A test item", "price": 10.99}
    response = client.post("/items/", json=item)
    assert response.status_code == 201
    assert response.json() == item