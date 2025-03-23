from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/links/shorten", response_model=schemas.LinkResponse)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = crud.create_link(db, link)
    return db_link

@router.get("/links/{short_code}")
def redirect_link(short_code: str, db: Session = Depends(get_db)):
    db_link = crud.get_link_by_short_code(db, short_code)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    crud.increment_link_access(db, db_link)
    return {"redirect_to": db_link.original_url}

@router.delete("/links/{short_code}")
def delete_link(short_code: str, db: Session = Depends(get_db)):
    crud.delete_link(db, short_code)
    return {"message": "Link deleted"}

# ==== app/routes/users.py ====
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

