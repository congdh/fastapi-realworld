# type: ignore
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    bio = Column(String, index=True)
    image = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
