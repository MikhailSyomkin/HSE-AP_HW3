from sqlalchemy.orm import Session
from app.models import Link
from app.services.shortener import generate_short_code
from datetime import datetime

def create_link(db: Session, original_url: str, custom_alias: str = None, expires_at: datetime = None):
    short_code = generate_short_code()
    db_link = Link(original_url=original_url, short_code=short_code, custom_alias=custom_alias, expires_at=expires_at)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def get_link_by_code(db: Session, short_code: str):
    return db.query(Link).filter(Link.short_code == short_code).first()

def update_link(db: Session, short_code: str, new_url: str):
    db_link = db.query(Link).filter(Link.short_code == short_code).first()
    db_link.original_url = new_url
    db.commit()
    return db_link

def delete_link(db: Session, short_code: str):
    db_link = db.query(Link).filter(Link.short_code == short_code).first()
    db.delete(db_link)
    db.commit()

def get_link_stats(db: Session, short_code: str):
    db_link = db.query(Link).filter(Link.short_code == short_code).first()
    return db_link

def get_link_by_original_url(db: Session, original_url: str):
    return db.query(Link).filter(Link.original_url == original_url).first()
