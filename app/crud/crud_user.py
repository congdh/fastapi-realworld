from typing import Optional

from sqlalchemy.orm import Session

from app import schemas, models
from app.core.security import verify_password, get_password_hash
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase[models.User, schemas.UserCreate, schemas.UserUpdate]):
    def get_user_by_email(self, db: Session, *, email: str) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.email == email).first()

    def create(self, db: Session, *, obj_in: schemas.UserCreate) -> models.User:
        db_obj = models.User(
            email=obj_in.email,
            username=obj_in.username,
            hashed_password=get_password_hash(obj_in.password),
            bio="",
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[models.User]:
        user = self.get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    async def get_user_by_username(self, db: Session, username: str) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.username == username).first()


user = CRUDUser(models.User)
