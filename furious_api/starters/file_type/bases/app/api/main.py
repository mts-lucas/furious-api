# importe suas rota da api aqui

from fastapi import APIRouter

from .routes import example

api_router = APIRouter()
api_router.include_router(example.router)