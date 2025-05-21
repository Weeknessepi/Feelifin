from fastapi import FastAPI, Response, Depends
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/sqlachemy")
def test(db: Session = Depends(get_db)):
    return {"Hello": "World"}

