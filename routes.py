from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

# books api's
from api import books

api_router.include_router(books.router)
