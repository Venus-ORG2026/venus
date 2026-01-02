from fastapi import APIRouter, Header, HTTPException
from app.database.firebase import verify_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me")
def get_me(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        user = verify_token(token)
        return {
            "uid": user["uid"],
            "email": user.get("email"),
            "name": user.get("name"),
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
