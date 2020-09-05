import pytest
from faker import Faker
from fastapi.encoders import jsonable_encoder
from pydantic.types import SecretStr
from sqlalchemy.orm import Session

from app import schemas, crud
from app.core import security


def test_create_user(db: Session) -> None:
    faker = Faker()
    profile = faker.profile()
    email = profile.get('mail', None)
    username = profile.get('username', None)
    password = 'changeit'

    user_in = schemas.UserCreate(username=username, email=email, password=SecretStr(password))
    user = crud.user.create(db=db, obj_in=user_in)
    assert user.email == email
    assert user.username == username
    assert hasattr(user, "hashed_password")
    assert security.verify_password(SecretStr(password), user.hashed_password)


def test_authenticate_user_success(db: Session) -> None:
    faker = Faker()
    profile = faker.profile()
    email = profile.get('mail', None)
    username = profile.get('username', None)
    password = 'changeit'

    user_in = schemas.UserCreate(username=username, email=email, password=SecretStr(password))
    user = crud.user.create(db=db, obj_in=user_in)

    wrong_email = email + 'xxx'
    authenticated_user = crud.user.authenticate(db, email=wrong_email, password=SecretStr(password))
    assert not authenticated_user

    wrong_password = password + 'xxx'
    authenticated_user = crud.user.authenticate(db, email=email, password=SecretStr(wrong_password))
    assert not authenticated_user

    authenticated_user = crud.user.authenticate(db, email=email, password=SecretStr(password))
    assert authenticated_user
    assert user.email == authenticated_user.email


@pytest.mark.parametrize("search_by", ('email', 'username', 'id'))
def test_get_user_by(db: Session, search_by: str) -> None:
    faker = Faker()
    profile = faker.profile()
    email = profile.get('mail', None)
    username = profile.get('username', None)
    password = 'changeit'

    user_in = schemas.UserCreate(username=username, email=email, password=SecretStr(password))
    user = crud.user.create(db=db, obj_in=user_in)
    func_name = f'get_user_by_{search_by}'
    func = getattr(crud.user, func_name)
    user_2 = func(db, getattr(user, search_by))
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)
