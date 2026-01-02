from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/books")
def books():
    return FileResponse("frontend/pages/books.html")
