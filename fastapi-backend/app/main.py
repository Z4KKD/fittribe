from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from passlib.context import CryptContext
from . import models, crud, auth
from .routes import auth, workout

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(workout.router, prefix="/workout", tags=["workout"])

class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    bio: str = None
    avatar: str = None
    fitness_goals: str = None

class UserLogin(BaseModel):
    email: str
    password: str

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    db_user = crud.create_user(db, user, hashed_password)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user or not auth.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = auth.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
