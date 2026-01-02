from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    # TODO: real auth
    if email and password:
        return RedirectResponse("/dashboard", status_code=302)
    return {"error": "Invalid login"}
