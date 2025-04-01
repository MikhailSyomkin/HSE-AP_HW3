from fastapi import FastAPI
from app.routes import links, users
from models import models

models.Base.metadata.create_all()

app = FastAPI(
    title="Link Shortener API",
    description="API для сокращения ссылок с возможностью получения статистики и управления ссылками.",
    version="1.0.0",
)

@app.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(links.router, prefix="/links", tags=["Links"])
app.include_router(users.router, prefix="/users", tags=["Users"])

