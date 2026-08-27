from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, default=1)
    price = Column(Float, nullable=True)
    is_bought = Column(Boolean, default=False)

    
    user_id = Column(Integer, ForeignKey("users.id"))