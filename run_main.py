from app import SqliteDatabase
from models.user import User
from models.tasks import Task
import time

db = SqliteDatabase(filename="tasks")
db.create_database()

LONG_DASH = "--------------------"
DOTS = "* * * * * * * * * * * *"


def check_passwd() -> tuple:
    user_email = input("Enter you email: ")
    user_passwd = input("Enter you password: ")
    result = db.check_password(users_email=user_email, user_passwd=user_passwd)
    return result, user_email


while True:
    print(LONG_DASH)
    choose = int(
        input(
            "--    MAIN MENU   --\nWhat you want to do?\n--------------------\n 1. Register a user.\n 2. Create a task.\n"
            " 3. Edit a user.\n 4. Edit a task.\n 5. Delete a user.\n 6. Delete a task.\n--------------------\nChoose number: "
        )
    )

    if choose == 1:
        user_name = input("Enter you name: ")
        user_surname = input("Enter you surname: ")
        user_email = input("Enter you email: ")
        user_passwd = input("Enter you password: ")
        db.register_user(
            users_name=user_name,
            users_surname=user_surname,
            users_email=user_email,
            users_passwd=user_passwd,
        )
        print("User registered !")
    if choose == 2:
        result = check_passwd()
        if result[0] == True:
            task = input("Enter task: ")
            # TODO add task_note
            db.create_task(user_email=result[1], task_name=task)

        else:
            print()
            print(DOTS)
            print("You must first register")
            print(DOTS)
            time.sleep(3.0)
    if choose == 3:
        result = check_passwd()
        if result[0] == True:
            change = int(
                input(
                    "--------------------\n-- EDIT USER MENU --\nWhat you want edit?\n--------------------\n1. Edit name.\n2. Edit surname.\n3. Edit email.\n4. Edit password.\n--------------------\nChoose a number: "
                )
            )
            get_user = db.session.query(User).filter_by(user_email=result[1]).first()
            if change == 1:  # change user name
                user_new_name = input("Write new name: ")
                get_user.user_name = user_new_name  #! #type:ignore
                db.session.commit()
                print("Name changed!")
            elif change == 2:  # change user name
                user_new_surname = input("Write new surname: ")
                get_user.user_surname = user_new_surname  #! #type:ignore
                db.session.commit()
                print("Surname changed!")
            elif change == 3:  # change user name
                user_new_email = input("Write new email: ")
                get_user.user_email = user_new_email  #! #type:ignore
                db.session.commit()
                print("Email changed!")
            elif change == 4:  # change user name
                user_new_passwd = input("Write new password: ")
                get_user.user_passwd = user_new_passwd  #! #type:ignore
                db.session.commit()
                print("Password changed!")
    if choose == 4:
        result = check_passwd()
        if result[0] == True:
            tasks = db.get_tasks(user_email=result[1])
            print("ID", "  Task name")
            tasks_id: list = []
            for n in tasks:
                print(
                    n.id,
                    "  ",
                    n.task_name,
                    n.task_note,
                    n.task_create_date,
                    n.task_finish_date,
                    n.task_status,
                )
                tasks_id.append(n.id)
            choose_task_id = int(
                input(
                    "--------------------\n-- EDIT TASK MENU --\nWhat task do you want edit?\n--------------------\nChoose a task id number: "
                )
            )
            if choose_task_id in tasks_id:
                editable_task = (
                    db.session.query(Task).filter_by(id=choose_task_id).first()
                )
                name = input(f"Change task name: {editable_task.task_name} Y/N -")
                if name.capitalize() == "Y":
                    edit_name = input("Edit tas name:")
                else:
                    edit_name = editable_task.task_name
                note = input(f"Change task note: {editable_task.task_note} Y/N -")
                if note.capitalize() == "Y":
                    edit_note = input("Edit task note:")
                else:
                    edit_note = editable_task.task_note
                finish_date = input(
                    f"Change task finish date: {editable_task.task_finish_date} Y/N -"
                )
                if finish_date.capitalize() == "Y":
                    edit_finish_date = input("Edit tas finish date:")
                else:
                    edit_finish_date = editable_task.task_finish_date
                status = input(f"Change task status: {editable_task.task_status} Y/N -")
                if status.capitalize() == "Y":
                    edit_status = input("Edit task status")
                else:
                    edit_status = editable_task.task_status
                db.change_task(
                    task_id=choose_task_id,
                    task_name=edit_name,
                    task_note=edit_note,
                    task_finished=edit_finish_date,
                    task_status=edit_status,
                )
            else:
                print("Wrond task ID")
    if choose == 5:
        result = check_passwd()
        if result[0] == True:
            user_id = db.get_users()

            one_id = int(input("Choose user id for delete: "))
            if one_id in user_id:
                db.delete_user(one_id)
            else:
                print("Wrong user ID !")
    if choose == 6:
        result = check_passwd()
        if result[0] == True:
            tasks = db.get_tasks(user_email=result[1])
            print("ID", "  Task name")
            tasks_id: list = []
            for n in tasks:
                print(
                    n.id,
                    "  ",
                    n.task_name,
                    n.task_note,
                    n.task_create_date,
                    n.task_finish_date,
                    n.task_status,
                )
                tasks_id.append(n.id)
            task_id = int(input("Choose task id for delete: "))
            if task_id in tasks_id:
                db.delete_user_task(task_id)
            else:
                print("Wrong task ID !")
