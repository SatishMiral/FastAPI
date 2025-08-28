from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a database url
# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Satish2512@localhost:5433/blog"

# create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a session local
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()