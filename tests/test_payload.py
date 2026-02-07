from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_payload():
    response = client.post(
        "/payload",
        json={
            "list_1": ["first string"],
            "list_2": ["other string"]
        }
    )

    assert response.status_code == 200
    payload_id = response.json()["id"]

    get_response = client.get(f"/payload/{payload_id}")
    assert get_response.status_code == 200
    assert get_response.json()["output"] == "FIRST STRING, OTHER STRING"
