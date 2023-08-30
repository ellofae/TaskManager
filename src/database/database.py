from decouple import config
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine(
    "postgresql+psycopg2://{}:{}@{}:{}/{}".format(*[config(a) for a in ['DATABASE_USER', 'DATABASE_PASSWORD', 'DATABASE_HOST', 'DATABASE_PORT', 'DATABASE_NAME']]),
    echo=True
)

# database base class wrapper
DatabaseBase = declarative_base()

# factory for session objects
SessionLocal = sessionmaker(bind=engine)

@contextmanager
def session():
    conn = SessionLocal()
    try:
        yield conn
    finally:
        conn.close()