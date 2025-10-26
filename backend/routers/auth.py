# backend/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from core.database import get_db, engine
from core.security import hash_password, verify_password
from models.user_model import User
from core.database import Base

# Asegurarse de crear las tablas en arranque (solo dev)
Base.metadata.create_all(bind=engine)

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

class LoginIn(BaseModel):
    username: str
    password: str

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Usuario o email ya registrado")
    hashed = hash_password(user.password)
    u = User(username=user.username, email=user.email, hashed_password=hashed)
    db.add(u)
    db.commit()
    db.refresh(u)
    # Corrección: acceder al valor del id directamente
    return UserOut(id=u.id, username=u.username, email=u.email)

@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Corrección: acceder al valor del id directamente
    return UserOut(id=user.id, username=user.username, email=user.email)

@router.post("/login")
def login(data: LoginIn, db: Session = Depends(get_db)):
    u = db.query(User).filter(User.username == data.username).first()
    if not u or not verify_password(data.password, u.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    # Aquí retornaríamos un JWT en entorno real; para pruebas devolvemos user id
    return {"message": "login ok", "user_id": u.id}
