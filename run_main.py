from app import SqliteDatabase
from models.user import User
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
            change = input(
                "--------------------\n-- EDIT USER MENU --\nWhat you want edit?\n--------------------\n1. Edit name.\n2. Edit surname.\n3. Edit email.\n4. Edit password.\n--------------------\nChoose a number: "
            )

        pass
