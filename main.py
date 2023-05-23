from database import SqliteDatabase


class ManageTasks:
    def __init__(self, base: SqliteDatabase) -> None:
        self.db = base
        self.db.create_database()

    def get_user(self, user_email: str) -> None:
        user = self.db.get_user(user_email=user_email)
        return user

    # def check_passwd() -> tuple:
    #     user_email = input("Enter you email: ")
    #     user_passwd = input("Enter you password: ")
    #     result = db.check_password(users_email=user_email, user_passwd=user_passwd)
    #     return result, user_email


manager = ManageTasks(SqliteDatabase("tasks"))


def run():
    user_email = input("Provide you registered email: ")
    manager.get_user(user_email=user_email)


run()
