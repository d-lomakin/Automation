from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
