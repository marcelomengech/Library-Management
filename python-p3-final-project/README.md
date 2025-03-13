# Library Management System CLI

## Description
A command-line interface (CLI) application for managing a library's collection of books and authors. This project demonstrates the use of SQLAlchemy ORM, Alembic migrations, and Click for CLI functionality.

## Features
- Author Management (CRUD operations)
  - Add new authors with biographies
  - List all authors
  - Update author information
  - Delete authors

- Book Management (CRUD operations)
  - Add new books with ISBN and publication year
  - List all books
  - Update book information
  - Delete books

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd python-p3-final-project
```

2. Create and activate virtual environment:
```bash
python -m venv new_venv
source new_venv/bin/activate
```

3. Install dependencies:
```bash
pip install click sqlalchemy alembic
```

4. Run database migrations:
```bash
alembic upgrade head
```

## Usage

### Basic Commands
```bash
# Show all available commands
python -m lib_cli.cli --help

# Author Management
python -m lib_cli.cli author add "Author Name" -b "Author Biography"
python -m lib_cli.cli author list
python -m lib_cli.cli author update 1 --name "New Name" --biography "New Bio"
python -m lib_cli.cli author delete 1

# Book Management
python -m lib_cli.cli book add "Book Title" 1 --isbn "1234567890" --year 2024
python -m lib_cli.cli book list
python -m lib_cli.cli book update 1 --title "New Title" --year 2025
python -m lib_cli.cli book delete 1
```

### Demo Script
Run the included demo script to see all features in action:
```bash
./demo.sh
```

## Project Structure
```
python-p3-final-project/
├── lib_cli/
│   ├── __init__.py
│   ├── cli.py
│   ├── db.py
│   └── models/
│       ├── __init__.py
│       ├── author.py
│       ├── book.py
│       └── genre.py
├── migrations/
├── alembic.ini
├── README.md
└── demo.sh
```

## Technologies Used
- Python
- SQLAlchemy ORM
- Alembic
- Click
- SQLite

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

