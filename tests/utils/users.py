from faker import Faker
from pydantic import SecretStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security

TEST_USER_PASSWORD = "changeit"


def get_test_user(db: Session) -> models.User:
    faker = Faker()
    profile = faker.profile()
    TEST_USER_EMAIL = profile.get("mail", None)
    TEST_USER_USERNAME = profile.get("username", None)
    user = crud.user.get_user_by_email(db=db, email=TEST_USER_EMAIL)
    if user is None:
        user_in = schemas.UserCreate(
            username=TEST_USER_USERNAME,
            email=TEST_USER_EMAIL,
            password=SecretStr(TEST_USER_PASSWORD),
        )
        user = crud.user.create(db=db, obj_in=user_in)
    return user


def get_test_user_token(test_user: models.User) -> str:
    return security.create_access_token(test_user.id)
