import pytest
from devtools import debug
from httpx import AsyncClient
from starlette import status


@pytest.mark.asyncio
async def test_user_login_failure(async_client: AsyncClient):
    login_data = {"user": {"email": "u1596352021", "password": "passwordxxx"}}
    r = await async_client.post(f"/api/users/login", json=login_data)
    user_response = r.json()
    debug(r.json())
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert "detail" in user_response
    assert user_response["detail"] == "Incorrect email or password"
