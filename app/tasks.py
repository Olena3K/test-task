from .celery_app import celery_app
from .db import SessionLocal, User, Address, CreditCard
import requests


@celery_app.task
def fetch_users():
    session = SessionLocal()
    response_user = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response_user.json()
    for u in data:
        user = User(id=u["id"], name=u["name"], email=u["email"])
        session.merge(user)
    session.commit()
    session.close()


@celery_app.task
def fetch_addresses():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        for user in users:
            response = requests.get(
                "https://random-data-api.com/api/address/random_address"
            )
            response.raise_for_status()
            addr = response.json()
            address = Address(
                user_id=user.id,
                street=addr.get("street_address"),
                city=addr.get("city"),
            )
            session.add(address)
        session.commit()
    finally:
        session.close()


@celery_app.task
def fetch_credit_cards():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        for user in users:
            response = requests.get(
                "https://random-data-api.com/api/credit_card/random_credit_card"
            )
            response.raise_for_status()
            card = response.json()
            credit_card = CreditCard(
                user_id=user.id,
                card_number=card.get("cc_number"),
                expiry=card.get("expiration_date"),
            )
            session.add(credit_card)
        session.commit()
    finally:
        session.close()
