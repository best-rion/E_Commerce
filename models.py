from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from eCommerce import db

class Admin(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)

class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    picture: Mapped[str] = mapped_column(String(25), unique=True, nullable=False, default='default.jpg')
