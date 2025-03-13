import click
from .db import get_session
from .models import Author, Book, Genre

@click.group()
def cli():
    """Library Management System CLI"""
    pass

# Author commands
@cli.group()
def author():
    """Manage authors"""
    pass

@author.command(name='add')
@click.argument('name')
@click.option('--biography', '-b', help='Author biography')
def add_author(name, biography):
    """Add a new author"""
    session = get_session()
    # Check if author already exists
    existing_author = session.query(Author).filter_by(name=name).first()
    if existing_author:
        click.echo(f'Author "{name}" already exists with ID: {existing_author.id}')
        return
    author = Author(name=name, biography=biography)
    session.add(author)
    session.commit()
    click.echo(f'Added author: {name}')

@author.command(name='list')  # Add name parameter to list command
def list_authors():
    """List all authors"""
    session = get_session()
    authors = session.query(Author).all()
    for author in authors:
        click.echo(f'ID: {author.id}, Name: {author.name}')

@author.command(name='update')
@click.argument('author_id', type=int)
@click.option('--name', help='New author name')
@click.option('--biography', '-b', help='New biography')
def update_author(author_id, name, biography):
    """Update an existing author"""
    session = get_session()
    author = session.query(Author).get(author_id)
    if not author:
        click.echo(f'Author with ID {author_id} not found')
        return
    if name:
        author.name = name
    if biography:
        author.biography = biography
    session.commit()
    click.echo(f'Updated author ID {author_id}')

@author.command(name='delete')
@click.argument('author_id', type=int)
def delete_author(author_id):
    """Delete an author"""
    session = get_session()
    author = session.query(Author).get(author_id)
    if not author:
        click.echo(f'Author with ID {author_id} not found')
        return
    session.delete(author)
    session.commit()
    click.echo(f'Deleted author ID {author_id}')

# Book commands
@cli.group()
def book():
    """Manage books"""
    pass

@book.command(name='add')
@click.argument('title')
@click.argument('author_id', type=int)
@click.option('--isbn', help='Book ISBN')
@click.option('--year', type=int, help='Publication year')
@click.option('--genres', help='Comma-separated genre names')
def add_book(title, author_id, isbn, year, genres):
    """Add a new book"""
    session = get_session()
    author = session.query(Author).get(author_id)
    if not author:
        click.echo(f'Author with ID {author_id} not found')
        return

    book = Book(
        title=title,
        author_id=author_id,
        isbn=isbn,
        publication_year=year
    )

    if genres:
        genre_names = [g.strip() for g in genres.split(',')]
        for genre_name in genre_names:
            genre = session.query(Genre).filter_by(name=genre_name).first()
            if not genre:
                genre = Genre(name=genre_name)
                session.add(genre)
            book.genres.append(genre)

    session.add(book)
    session.commit()
    click.echo(f'Added book: {title}')

@book.command(name='list')
def list_books():
    """List all books"""
    session = get_session()
    books = session.query(Book).all()
    for book in books:
        genres = ', '.join(genre.name for genre in book.genres)
        click.echo(f'ID: {book.id}, Title: {book.title}, Author: {book.author.name}, Genres: {genres}')

@book.command(name='update')  # Add name parameter to update command
@click.argument('book_id', type=int)
@click.option('--title', help='New book title')
@click.option('--author-id', type=int, help='New author ID')
@click.option('--isbn', help='New ISBN')
@click.option('--year', type=int, help='New publication year')
@click.option('--genres', help='Comma-separated genre names')
def update_book(book_id, title, author_id, isbn, year, genres):
    """Update an existing book"""
    session = get_session()
    book = session.query(Book).get(book_id)

    if not book:
        click.echo(f'Book with ID {book_id} not found')
        return

    if title:
        book.title = title
    if author_id:
        if not session.query(Author).get(author_id):
            click.echo(f'Author with ID {author_id} not found')
            return
        book.author_id = author_id
    if isbn:
        book.isbn = isbn
    if year:
        book.publication_year = year

    if genres:
        book.genres = []
        genre_names = [g.strip() for g in genres.split(',')]
        for genre_name in genre_names:
            genre = session.query(Genre).filter_by(name=genre_name).first()
            if not genre:
                genre = Genre(name=genre_name)
                session.add(genre)
            book.genres.append(genre)

    session.commit()
    click.echo(f'Updated book ID {book_id}')

@book.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    """Delete a book"""
    session = get_session()
    book = session.query(Book).get(book_id)
    if not book:
        click.echo(f'Book with ID {book_id} not found')
        return
    session.delete(book)
    session.commit()
    click.echo(f'Deleted book ID {book_id}')

# Genre commands
@cli.group()
def genre():
    """Manage genres"""
    pass

@genre.command(name='add')  # Add name parameter
@click.argument('name')
def add_genre(name):
    """Add a new genre"""
    session = get_session()
    # Check if genre already exists
    existing_genre = session.query(Genre).filter_by(name=name).first()
    if existing_genre:
        click.echo(f'Genre "{name}" already exists with ID: {existing_genre.id}')
        return
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    click.echo(f'Added genre: {name}')

@genre.command(name='list')  # Add the name parameter
def list_genres():
    """List all genres"""
    session = get_session()
    genres = session.query(Genre).all()
    for genre in genres:
        click.echo(f'ID: {genre.id}, Name: {genre.name}')

@genre.command()
@click.argument('genre_id', type=int)
@click.option('--name', help='New genre name')
def update_genre(genre_id, name):
    """Update an existing genre"""
    session = get_session()
    genre = session.query(Genre).get(genre_id)
    if not genre:
        click.echo(f'Genre with ID {genre_id} not found')
        return
    if name:
        genre.name = name
    session.commit()
    click.echo(f'Updated genre ID {genre_id}')

@genre.command()
@click.argument('genre_id', type=int)
def delete_genre(genre_id):
    """Delete a genre"""
    session = get_session()
    genre = session.query(Genre).get(genre_id)
    if not genre:
        click.echo(f'Genre with ID {genre_id} not found')
        return
    session.delete(genre)
    session.commit()
    click.echo(f'Deleted genre ID {genre_id}')

if __name__ == '__main__':
    cli()