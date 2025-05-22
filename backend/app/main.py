from fastapi import FastAPI, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, oauth2
from .database import engine, get_db
from .schemas import UserCreate, Token
from .utils import hash, verify

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/sqlachemy")
def test(db: Session = Depends(get_db)):
    return {"Hello": "World"}

@app.get("/health")
def health():
    return Response(status_code=200)

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        return user
    else:
        return Response(status_code=404)
    
@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login", response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
    if not user:
        return Response(status_code=404)
    if not verify(user_credentials.password, user.hashed_password):
        return Response(status_code=401)
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
def get_current_user(user_id: int = Depends(oauth2.get_current_user)):
    return user_id

@app.get("/test")
def get_current_user(user_id: int = Depends(oauth2.get_current_user)):
    return "test"