from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="group")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    phone = Column(String, unique=True, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_teacher = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    photo = Column(String, nullable=True)
    group_id = Column(Integer, ForeignKey("groups.id"))

    group = relationship("Group", back_populates="users")

    journal_entries = relationship("Journal", back_populates="user")


class Journal(Base):
    __tablename__ = 'journal'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    lesson_number = Column(Integer, nullable=False)  # Пара (1-7)
    status = Column(String(10), nullable=False)  # "присутствовал", "опоздал", "отсутствовал"

    user = relationship("User", back_populates="journal_entries")
