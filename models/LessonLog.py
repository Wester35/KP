from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from libs.database import Base


class LessonLog(Base):
    __tablename__ = 'lesson_log'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
    lesson_number = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    lesson_data = Column(String, nullable=True)

    teacher = relationship("User", foreign_keys=[teacher_id])
    group = relationship("Group", foreign_keys=[group_id])
