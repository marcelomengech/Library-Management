from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the base class for declarative models
Base = declarative_base()

# Create database engine
engine = create_engine('sqlite:///library.db')

# Create session factory
Session = sessionmaker(bind=engine)

def init_db():
    """Initialize the database, creating all tables."""
    Base.metadata.create_all(engine)

def get_session():
    """Get a new database session."""
    return Session()