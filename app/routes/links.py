from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, services
from app.schemas import LinkCreate, LinkStats
from models import models

router = APIRouter()

@router.post("/shorten")
def shorten_link(link: LinkCreate, db: Session = Depends(get_db)):
    if link.custom_alias:
        if not services.is_alias_unique(db, link.custom_alias):
            raise HTTPException(status_code=400, detail="Custom alias is not unique.")
    db_link = crud.create_link(db, original_url=link.original_url, custom_alias=link.custom_alias, expires_at=link.expires_at)
    return {"short_code": db_link.short_code, "original_url": db_link.original_url}

@router.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_link = crud.get_link_by_code(db, short_code)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    db_link.access_count += 1
    db_link.last_accessed = datetime.utcnow()
    db.commit()
    return {"redirect_to": db_link.original_url}

@router.delete("/{short_code}")
def delete_link(short_code: str, db: Session = Depends(get_db)):
    db_link = crud.get_link_by_code(db, short_code)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    crud.delete_link(db, short_code)
    return {"message": "Link deleted successfully"}

@router.put("/{short_code}")
def update_link(short_code: str, new_url: str, db: Session = Depends(get_db)):
    db_link = crud.get_link_by_code(db, short_code)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    updated_link = crud.update_link(db, short_code, new_url)
    return {"short_code": updated_link.short_code, "new_url": updated_link.original_url}

@router.get("/{short_code}/stats", response_model=LinkStats)
def get_link_stats(short_code: str, db: Session = Depends(get_db)):
    db_link = crud.get_link_stats(db, short_code)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link
