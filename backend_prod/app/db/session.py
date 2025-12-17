
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./phase4.db")
engine = create_engine(DATABASE_URL, echo=True)
