# importe suas rota da api aqui

from app.api.routes import example
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(example.router)