from app import SqliteDatabase
from models.user import User


while True:
    choose = int(
        input(
            "What you want to do:\n 1. Register a user:\n 2. Create a task:\n"
            " 3. Edit a user:\n 4. Edit a task:\n 5. Delete a user:\n 6. Delete a task:\n Choose number: "
        )
    )
    if choose == 1:
        user_name = input("Enter you name: ")
        user_surname = input("Enter you surname: ")
        user_email = input("Enter you email: ")
        user_passwd = input("Enter you password: ")
        db.register_user(
            user_name=user_name,
            user_surname=user_surname,
            user_email=user_email,
            user_passwd=user_passwd,
        )
