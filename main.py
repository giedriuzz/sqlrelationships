from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from db.base import Base

from models.user import User
from models.tasks import Task


engine = create_engine("sqlite:///tasks_new.db")
Base.metadata.create_all(engine, checkfirst=True)
