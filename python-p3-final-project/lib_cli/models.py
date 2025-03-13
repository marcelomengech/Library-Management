from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .db import Base

# Association table for many-to-many relationship between books and genres
book_genre = Table(
    'book_genre',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    biography = Column(String)

    # Relationship with Book
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author(name='{self.name}')>"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    isbn = Column(String, unique=True)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))

    # Relationships
    author = relationship('Author', back_populates='books')
    genres = relationship('Genre', secondary=book_genre, back_populates='books')

    def __repr__(self):
        return f"<Book(title='{self.title}')>"

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Relationship with Book
    books = relationship('Book', secondary=book_genre, back_populates='genres')

    def __repr__(self):
        return f"<Genre(name='{self.name}')>"