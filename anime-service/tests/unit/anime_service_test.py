from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_animes():
    response = client.get("/api/v1/animes/", headers={"accept": "application/json"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_create_anime_success():
    success_anime_data = {
        "name": "TestAnime",
        "plot": "TestAnimePlot",
        "genres": [
            "TestGenre"
        ],
        "casts_id": [
            1
        ]
    }
    response = client.post("/api/v1/animes/", json=new_anime_data, headers={"accept": "application/json", "Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["name"] == "string"

def test_create_anime_failure():
    failure_anime_data = {
        "name": "FailureAnime",
        "plot": "FailureAnimePlot",
        "genres": "NotArray",
        "casts_id": [
            1
        ]
    }
    response = client.post("/api/v1/animes/", json=wrong_anime_data, headers={"accept": "application/json", "Content-Type": "application/json"})
    assert response.status_code == 422

def get_anime_by_id_success():
    response = client.get("/api/v1/animes/1/", headers={"accept": "application/json"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["id"] == 1

def get_anime_by_id_failure():
    response = client.get("/api/v1/animes/999/", headers={"accept": "application/json"})
    assert response.status_code == 404

def update_anime_success():
    payload = {
        "name": "string",
        "plot": "string",
        "genres": [
            "string"
        ],
        "casts_id": [
            1
        ]
    }
    response = client.put("/api/v1/animes/1/", headers={"accept": "application/json", "Content-Type": "application/json"}, json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def update_anime_failure():
    payload = {
        "name": "string",
        "plot": "string",
        "genres": [
            "string"
        ],
        "casts_id": [
            1
        ]
    }
    response = client.put("/api/v1/animes/999/", headers={"accept": "application/json","Content-Type": "application/json"}, json=payload)
    assert response.status_code == 404

def delete_anime_success():
    response = client.delete("/api/v1/animes/1/", headers={"accept": "application/json"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def delete_anime_failure():
    response = client.delete("/api/v1/animes/999/", headers={"accept": "application/json"})
    assert response.status_code == 404