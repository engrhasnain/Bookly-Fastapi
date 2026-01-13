from db.db import books_date
from fastapi import APIRouter


router = APIRouter(prefix="/books", tags=["Book CRUD"])

from models.books import BookCreated, BookResponse
from typing import List


@router.get("/get", response_model=List[BookResponse])
async def get_books():
    return books_date

@router.post("/create", response_model=BookResponse)
async def create_book(book: BookCreated):
    new_book = book.model_dump()
    new_book["id"] = len(books_date) + 1
    books_date.append(new_book)
    return BookResponse(**new_book)