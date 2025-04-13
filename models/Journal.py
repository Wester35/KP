from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from libs.database import Base


class Journal(Base):
    __tablename__ = 'journal'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    lesson_number = Column(Integer, nullable=False)
    status = Column(String(10), nullable=False)
    teacher_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    student = relationship("User", foreign_keys=[user_id], back_populates="journal_entries_as_student")
    teacher = relationship("User", foreign_keys=[teacher_id], back_populates="journal_entries_as_teacher")
