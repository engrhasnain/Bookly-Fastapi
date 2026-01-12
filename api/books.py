from db.db import books_date
from fastapi import APIRouter


router = APIRouter(prefix="/books", tags=["Book CRUD"])


@router.get("/get")
async def get_books():
    return books_date


from models.books import BookCreated, BookResponse

@router.post("/create", response_model=BookResponse)
async def create_book(book: BookCreated):
    new_book = book.model_dump()
    new_book["id"] = len(books_date) + 1
    books_date.append(new_book)
    return BookResponse(**new_book)