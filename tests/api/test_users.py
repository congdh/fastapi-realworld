from typing import Dict

from fastapi import status
from fastapi.testclient import TestClient
from faker import Faker


def test_user_login_failure(client: TestClient):
    login_data = {"user": {"email": "u1596352021", "password": "passwordxxx"}}
    r = client.post(f"/api/users/login", json=login_data)
    user_response = r.json()
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert "detail" in user_response
    assert user_response['detail'] == 'Incorrect email or password'


def test_register_success(client: TestClient):
    password = 'password'
    faker = Faker()
    profile = faker.profile()
    email = profile.get('mail', None)
    username = profile.get('username', None)
    user_in = {"user": {"email": email, "password": password, "username": username}}
    r = client.post(f"/api/users", json=user_in)
    user_response = r.json()
    assert r.status_code == status.HTTP_200_OK
    assert 'user' in user_response
    user_with_token = user_response.get('user')
    assert isinstance(user_with_token, Dict)
    assert 'email' in user_with_token
    assert user_with_token['email'] == email
    assert 'username' in user_with_token
    assert user_with_token['username'] == username
    assert 'token' in user_with_token
    assert 'bio' in user_with_token


def test_register_failure_by_existed_user(client: TestClient):
    password = 'password'
    faker = Faker()
    profile = faker.profile()
    email = profile.get('mail', None)
    username = profile.get('username', None)
    user_in = {"user": {"email": email, "password": password, "username": username}}
    r = client.post(f"/api/users", json=user_in)
    assert r.status_code == status.HTTP_200_OK

    r = client.post(f"/api/users", json=user_in)
    user_response = r.json()
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert "detail" in user_response
    assert user_response['detail'] == "The user with this username already exists in the system."
