from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class LinkBase(BaseModel):
    original_url: HttpUrl
    short_code: Optional[str] = None
    expires_at: Optional[datetime] = None

class LinkCreate(LinkBase):
    pass

class LinkResponse(LinkBase):
    id: int
    created_at: datetime
    last_accessed: Optional[datetime]
    access_count: int
    user_id: Optional[int]

    class Config:
        from_attributes = True
