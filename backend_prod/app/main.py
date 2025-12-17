
from fastapi import FastAPI

app = FastAPI(title="Cube-One Phase 4 Accounting")

@app.get("/")
def root():
    return {"status": "Cube-One Phase 4 Accounting Engine Running"}
