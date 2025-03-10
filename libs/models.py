from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from datetime import date
from .database import Base
import enum


class RoleEnum(str, enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    full_name = Column(String, nullable=False)
    group = Column(String, nullable=True)
    photo = Column(LargeBinary, nullable=True)

    attendance_records = relationship("Attendance", back_populates="student")


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, default=date.today, nullable=False)
    pair_number = Column(Integer, nullable=False)
    is_late = Column(Boolean, default=False)

    student = relationship("User", back_populates="attendance_records")