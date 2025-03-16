from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .models import Base


DATABASE_URL = "postgresql://postgres:0302@localhost/KP"


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Создает таблицы в БД, если их нет"""
    Base.metadata.create_all(engine)
