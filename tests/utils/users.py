from faker import Faker
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.core import security

faker = Faker()
profile = faker.profile()
TEST_USER_EMAIL = profile.get('mail', None)
TEST_USER_USERNAME = profile.get('username', None)
TEST_USER_PASSWORD = 'password'


def create_test_user(db: Session) -> models.User:
    user_in = schemas.UserCreate(username=TEST_USER_USERNAME, email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD)
    user = crud.user.create(db=db, obj_in=user_in)
    return user


def get_test_user(db: Session) -> models.User:
    user = crud.user.get_user_by_email(db=db, email=TEST_USER_EMAIL)
    if user is None:
        user = create_test_user(db)
    return user


def get_test_user_token(test_user: models.User) -> str:
    return security.create_access_token(test_user.id)
