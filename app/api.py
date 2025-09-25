from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal, User, Address, CreditCard, init_db

app = FastAPI()

init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.get("/users/{user_id}/addresses")
def read_addresses(user_id: int, db: Session = Depends(get_db)):
    return db.query(Address).filter(Address.user_id == user_id).all()


@app.get("/users/{user_id}/creditcards")
def read_credit_cards(user_id: int, db: Session = Depends(get_db)):
    return db.query(CreditCard).filter(CreditCard.user_id == user_id).all()
