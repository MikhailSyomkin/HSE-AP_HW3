HSE-AP_HW3


==== Файловая структура проекта ====
├── app/

│   ├── main.py  # Точка входа \n
│   ├── config.py  # Конфигурации
│   ├── database.py  # Подключение к БД
│   ├── models.py  # Описание таблиц SQLAlchemy
│   ├── schemas.py  # Pydantic-схемы
│   ├── crud.py  # Операции с БД
│   ├── routes/
│   │   ├── links.py  # Эндпоинты для ссылок
│   │   ├── users.py  # Эндпоинты для пользователей
│   └── services/
│       ├── shortener.py  # Логика сокращения ссылок
│       ├── cache.py  # Работа с Redis
├── alembic/  # Миграции БД
├── .env  # Переменные окружения
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
