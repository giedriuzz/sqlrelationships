from app import SqliteDatabase
from models.user import User

db = SqliteDatabase(filename="tasks")
db.create_database()

LONG_DOTS = "--------------------"
while True:
    print(LONG_DOTS)
    choose = int(
        input(
            "What you want to do?\n--------------------\n 1. Register a user:\n 2. Create a task:\n"
            " 3. Edit a user:\n 4. Edit a task:\n 5. Delete a user:\n 6. Delete a task:\n--------------------\nChoose number: "
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
