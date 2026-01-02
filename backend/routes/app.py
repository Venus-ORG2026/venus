from fastapi import APIRouter, Header
from app.database.firebase import db, verify_token

router = APIRouter(prefix="/app", tags=["app"])

@router.get("/books")
def list_books(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    user = verify_token(token)

    books_ref = db.collection("books").where("status", "==", "published")
    books = [doc.to_dict() for doc in books_ref.stream()]

    return books
