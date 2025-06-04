from app.core.config import settings
from app.core.database import create_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    app.add_middleware(CORSMiddleware, **settings.CORS_CONFIG)
    create_tables()
    return app


app = start_application()