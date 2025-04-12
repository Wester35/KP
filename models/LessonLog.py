from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class LessonLog(Base):
    __tablename__ = 'lesson_log'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    lesson_number = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)