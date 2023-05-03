from for_tests.old_sessions import session
from models.tasks import Task
from models.user import User

user_1 = session.query(User).get(1)  # get first user from User table
user_1.user_name = "Tadas"  # new name to user
session.commit()
