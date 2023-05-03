from models.user import User
from models.tasks import Task
from for_tests.old_sessions import session


task_1 = Task(task_name="Geras darbas 1")  # make a task_1
task_2 = Task(task_name="Blogas darbas")  # make a task_2
user_1 = User(
    user_name="Giedrius", user_surname="Kulis"
)  # create a user for assign task_1 and task_2

print(user_1.tasks.append(task_1))  #
print(user_1.tasks.append(task_2))

session.add(user_1)
session.commit()
