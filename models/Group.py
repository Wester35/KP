from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Date, Time
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from libs.database import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="group")