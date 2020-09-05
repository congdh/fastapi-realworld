from typing import Optional

from pydantic import EmailStr, BaseModel, HttpUrl, SecretStr, Field


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = Field(None, example='sheilaavery@yahoo.com')
    username: Optional[str] = Field(None, example="perryshari")
    bio: Optional[str] = None
    image: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr = Field(..., example='sheilaavery@yahoo.com')
    username: str = Field(..., example="perryshari")
    password: SecretStr = Field(..., example='changeit')


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = Field(None, example='changeit')


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


# Additional properties to return via API
# class User(UserInDBBase):
#     pass


class UserWithToken(UserBase):
    token: str = Field(...,
                       example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTk3MjI3MTIsInN1YiI6IjEifQ.cTWIopIYrXLEeRix_sTiqx6RRBuXG4a6xVUcMKyovWA")


class UserResponse(BaseModel):
    user: UserWithToken


class LoginUser(BaseModel):
    email: str
    password: SecretStr

    class Config:
        schema_extra = {
            "example": {
                "email": "ahart@yahoo.com",
                "password": "changeit",
            }
        }


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None
