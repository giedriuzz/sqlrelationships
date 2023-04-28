from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tasks import Task
from models.user import User

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
session = Session()
