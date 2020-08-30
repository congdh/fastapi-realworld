from fastapi.testclient import TestClient


def test_read_users(client: TestClient):
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [{'username': 'Foo'}, {'username': 'Bar'}]
