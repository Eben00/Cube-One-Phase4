from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.models import Account

router=APIRouter()

@router.post("/")
def create(code:str,name:str,type:str,s:Session=Depends(get_session)):
    a=Account(code=code,name=name,type=type)
    s.add(a);s.commit()
    return a

@router.get("/")
def list(s:Session=Depends(get_session)):
    return s.exec(select(Account)).all()
