from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tasks import Task
from models.user import User
from db.base import Base

engine = create_engine("sqlite:///tasks_new.db")
Session = sessionmaker(bind=engine)
session = Session()
