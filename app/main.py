from fastapi import FastAPI
from app.routes import links, users

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(links.router, prefix="/links", tags=["Links"])
app.include_router(users.router, prefix="/users", tags=["Users"])
