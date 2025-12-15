from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
from app.api import auth, users, accounts

app = FastAPI(title="Dealer System – Phase 4")

@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(accounts.router, prefix="/accounts")

@app.get("/")
def root():
    return {"phase": 4}
