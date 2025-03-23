from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_links():
    return {"message": "Links endpoint"}
