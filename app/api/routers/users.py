from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.status import HTTP_400_BAD_REQUEST

from app import schemas, crud, models
from app.api import deps
from app.core import security

router = APIRouter()


@router.post("", name="Register a new user", response_model=schemas.UserResponse)
async def register(
        user_in: schemas.UserCreate = Body(
            ..., embed=True, alias="user"),
        db: Session = Depends(deps.get_db)
) -> schemas.UserResponse:
    user = crud.user.get_user_by_email(db, email=user_in.email)
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


@router.get("", name="Get current user", response_model=schemas.UserResponse)
async def retrieve_current_user(
        current_user: models.User = Depends(deps.get_current_user)
) -> schemas.UserResponse:
    token = security.create_access_token(
        current_user.id
    )
    return schemas.UserResponse(
        user=schemas.UserWithToken(
            username=current_user.username,
            email=current_user.email,
            bio=current_user.bio,
            image=current_user.image,
            token=token
        )
    )


@router.put("", name="Update current user", response_model=schemas.UserResponse)
async def update_current_user(
        user_update: schemas.UserInUpdate = Body(
            ..., embed=True, alias="user"),
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
) -> schemas.UserResponse:
    if user_update.username and user_update.username != current_user.username:
        user = crud.user.get_user_by_username(
            db, username=user_update.username)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="user with this username already exists",
            )
    if user_update.email and user_update.email != current_user.email:
        user = crud.user.get_user_by_email(
            db, email=user_update.email)
        if user:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="user with this email already exists",
            )
    user = crud.user.update(db, db_obj=current_user, obj_in=user_update)
    token = security.create_access_token(
        user.id
    )
    return schemas.UserResponse(
        user=schemas.UserWithToken(
            username=user.username,
            email=user.email,
            bio=user.bio,
            image=user.image,
            token=token
        )
    )
