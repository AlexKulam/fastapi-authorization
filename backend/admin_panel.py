from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.data_base import SessionLocal, User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/admin")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"username": u.username, "email": u.email} for u in users]
