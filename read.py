from models.tasks import Task
from models.user import User
from old_sessions import session

user_1 = session.query(User).get(1)  # get firs user from table User
for task in user_1.tasks:  # iterate user in tasks
    print(task.task_name)  # print gets user tasks
