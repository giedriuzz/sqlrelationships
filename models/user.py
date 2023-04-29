from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from db.base import Base  # import Base from /db/base/base.py


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column("name", String)
    user_surname = Column("surname", String)
    user_email = Column("email", String, unique=True)  # only unique values in column
    passwd = Column("password", String)
    tasks = relationship("Task", back_populates="users")
