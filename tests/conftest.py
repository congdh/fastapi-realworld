from typing import Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app import models
from app.db.session import SessionLocal
from app.main import app
from .utils.users import get_test_user, get_test_user_token


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
async def async_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture
def test_user(db: Session) -> models.User:
    return get_test_user(db)


@pytest.fixture
def token(test_user: models.User) -> str:
    return get_test_user_token(test_user)
