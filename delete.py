from sessions import session
from models.tasks import Task
from models.user import User

task_1 = session.query(Task).get(2)  # delete task whose id is 2
session.delete(task_1)
session.commit()
