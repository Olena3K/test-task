from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200


def test_read_addresses():
    response = client.get("/users/1/addresses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_creditcards():
    response = client.get("/users/1/creditcards")
    assert response.status_code == 200
    assert isinstance(response.json(), list)