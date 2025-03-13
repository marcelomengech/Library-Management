# Library Management System CLI Package

from .models import Author, Book, Genre
from .cli import cli

__all__ = ['cli']
from .db import init_db

__version__ = '0.1.0'