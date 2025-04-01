from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, unique=True, index=True)
    short_code = Column(String, unique=True, index=True)
    custom_alias = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    last_accessed = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", nullable=True))
    user = relationship("User", back_populates="links")
    access_count = Column(Integer, default=0)  # Количество переходов
