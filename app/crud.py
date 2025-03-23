from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
from typing import Optional

# ===== CRUD для пользователей =====
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # TODO: добавить хеширование
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# ===== CRUD для ссылок =====
def create_link(db: Session, link: schemas.LinkCreate, user_id: Optional[int] = None):
    db_link = models.Link(
        original_url=link.original_url,
        short_code=link.short_code,
        expires_at=link.expires_at,
        user_id=user_id,
    )
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def get_link_by_short_code(db: Session, short_code: str):
    return db.query(models.Link).filter(models.Link.short_code == short_code).first()

def increment_link_access(db: Session, link: models.Link):
    link.access_count += 1
    link.last_accessed = datetime.utcnow()
    db.commit()
    db.refresh(link)
    return link

def delete_link(db: Session, short_code: str):
    db.query(models.Link).filter(models.Link.short_code == short_code).delete()
    db.commit()
