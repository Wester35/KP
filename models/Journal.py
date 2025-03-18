from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from libs.database import Base


class Journal(Base):
    __tablename__ = 'journal'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    lesson_number = Column(Integer, nullable=False)  # Пара (1-7)
    status = Column(String(10), nullable=False)  # "присутствовал", "опоздал", "отсутствовал"

    user = relationship("User", back_populates="journal_entries")