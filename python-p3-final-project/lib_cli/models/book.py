from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

book_genre = Table(
    'book_genres',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    isbn = Column(String(13))
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    author = relationship('Author', back_populates='books')
    genres = relationship('Genre', secondary=book_genre, back_populates='books')