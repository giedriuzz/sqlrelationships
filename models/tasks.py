from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from db.base import Base  # import Base from /db/base/base.py


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task_name = Column("task", String)
    task_note = Column("note", String)
    task_create_date = Column("task create date", DateTime)
    task_finish_date = Column("task finish date", DateTime)
    task_status = Column("status", String)
    task_id = Column(Integer, ForeignKey("user.id"))
    users = relationship("User", back_populates="tasks")
