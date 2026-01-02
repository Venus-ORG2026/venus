from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return FileResponse("frontend/pages/dashboard.html")
