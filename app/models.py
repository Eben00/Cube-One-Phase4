from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int]=Field(default=None,primary_key=True)
    username:str=Field(unique=True)
    password_hash:str
    role:str="user"

class Account(SQLModel, table=True):
    id: Optional[int]=Field(default=None,primary_key=True)
    code:str=Field(unique=True)
    name:str
    type:str
