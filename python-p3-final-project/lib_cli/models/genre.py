from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .book import book_genre

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    books = relationship('Book', secondary=book_genre, back_populates='genres')