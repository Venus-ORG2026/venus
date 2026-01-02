from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routes import login, register, books, dashboard

app = FastAPI()

app.include_router(login.router)
app.include_router(register.router)
app.include_router(books.router)
app.include_router(dashboard.router)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
