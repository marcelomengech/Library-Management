from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import Base

DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def init_db():
    Base.metadata.create_all(engine)