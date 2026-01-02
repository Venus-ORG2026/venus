from pydantic import BaseModel

class User(BaseModel):
    uid: str
    email: str | None
    displayName: str | None
    photoURL: str | None = None
