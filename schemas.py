from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LinkCreate(BaseModel):
    original_url: str
    custom_alias: Optional[str] = None
    expires_at: Optional[datetime] = None

class LinkStats(BaseModel):
    original_url: str
    short_code: str
    created_at: datetime
    access_count: int
    last_accessed: Optional[datetime] = None
