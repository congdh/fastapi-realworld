from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.core import security

router = APIRouter()


@router.post("", name="Register a new user", response_model=schemas.UserResponse)
async def register(
        user_in: schemas.UserCreate = Body(
            ..., embed=True, alias="user"),
        db: Session = Depends(deps.get_db)
) -> schemas.UserResponse:
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    token = security.create_access_token(user.id)
    return schemas.UserResponse(
        user=schemas.UserWithToken(
            username=user.username,
            email=user.email,
            bio=user.bio,
            image=user.image,
            token=token
        )
    )


@router.post("/login", name="Login and Remember Token", response_model=schemas.UserResponse)
async def login(
        user_login: schemas.LoginUser = Body(..., embed=True,
                                             alias="user", name="Credentials to use"),
        db: Session = Depends(deps.get_db)
) -> schemas.UserResponse:
    user = crud.user.authenticate(
        db, email=user_login.email, password=user_login.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = security.create_access_token(user.id)
    return schemas.UserResponse(
        user=schemas.UserWithToken(
            username=user.username,
            email=user.email,
            bio=user.bio,
            image=user.image,
            token=token
        )
    )
