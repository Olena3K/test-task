from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@db:5432/test_task"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    credit_cards = relationship(
        "CreditCard", back_populates="user", cascade="all, delete-orphan"
    )
    __table_args__ = (CheckConstraint("id > 0", name="check_user_id_positive"),)


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    street = Column(String(200), nullable=False)
    city = Column(String(100), nullable=False)
    user = relationship("User", back_populates="addresses")
    __table_args__ = (CheckConstraint("id > 0", name="check_address_id_positive"),)


class CreditCard(Base):
    __tablename__ = "credit_cards"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    card_number = Column(String(20), nullable=False)
    expiry = Column(String(10), nullable=False)
    user = relationship("User", back_populates="credit_cards")
    __table_args__ = (CheckConstraint("id > 0", name="check_creditcard_id_positive"),)


def init_db():
    Base.metadata.create_all(bind=engine)
