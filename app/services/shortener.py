import random
import string
from datetime import datetime

def generate_short_code(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_alias_unique(db, alias: str) -> bool:
    return db.query(Link).filter(Link.custom_alias == alias).first() is None

def check_expiry(db_link, current_time: datetime) -> bool:
    if db_link.expires_at and db_link.expires_at < current_time:
        return True
    return False
