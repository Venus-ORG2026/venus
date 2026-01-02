from pydantic import BaseModel

class Book(BaseModel):
    id: str
    title: str
    description: str
    authorId: str
    status: str
