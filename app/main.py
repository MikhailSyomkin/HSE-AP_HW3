from fastapi import FastAPI
from app.routes import links, users
from app.database import engine
from app import models
from app.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Link Shortener API",  # Заголовок API
    description="API для сокращения ссылок с возможностью получения статистики и управления ссылками.",
    version="1.0.0",
)

@app.get("/ping")
def ping():
    return {"message": "pong"}

# Подключаем роутеры для ссылок и пользователей
app.include_router(links.router, prefix="/links", tags=["Links"])
app.include_router(users.router, prefix="/users", tags=["Users"])

