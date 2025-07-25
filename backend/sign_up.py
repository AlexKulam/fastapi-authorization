from fastapi import APIRouter, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from backend.data_base import SessionLocal, User
from passlib.hash import bcrypt

router = APIRouter

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("signup")
def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
                  ):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Такое имя уже существует")
    
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Такая почта уже используется")
    
    hashed_password = bcrypt.hash(password)

    user = User(username=username, email=email, password=hashed_password)
    db.add(user)
    db.commit()

    return {"message": "Пользователь успешно зарегистрирован"}
