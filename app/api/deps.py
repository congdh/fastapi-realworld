from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from starlette import status

from app import crud, models
from app.core import security
from app.db.session import SessionLocal

JWT_TOKEN_PREFIX = "Token"  # noqa: S105


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def authrization_heder_token(
    api_key: str = Depends(APIKeyHeader(name="Authorization")),
) -> str:
    try:
        token_prefix, token = api_key.split(" ")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="unsupported authorization type",
        )
    if token_prefix != JWT_TOKEN_PREFIX:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="unsupported authorization type",
        )
    return token


async def get_current_user(
    token: str = Depends(authrization_heder_token), db: Session = Depends(get_db)
) -> models.User:
    user_id = security.get_user_id_from_token(token=token)
    user = crud.user.get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
