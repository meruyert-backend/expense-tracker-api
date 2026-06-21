from fastapi import FastAPI

from database import Base, engine
from routers import expenses

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(expenses.router)


@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}