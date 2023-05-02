from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError  # error handling
from db.base import Base
from datetime import datetime, time
from models.user import User
from models.tasks import Task


class SqliteDatabase:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.engine = create_engine(f"sqlite:///{self.filename}.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_database(self):
        Base.metadata.create_all(self.engine, checkfirst=True)

    def register_user(
        self, users_name: str, users_surname: str, users_email: str, users_passwd: str
    ) -> None:
        """_summary_

        Args:
            user_name (str): _description_
            user_surname (str): _description_
            user_email (str): _description_
            user_passwd (str): _description_
        """ """"""

        user_1 = User(
            user_name=users_name,
            user_surname=users_surname,
            user_email=users_email,
            user_passwd=users_passwd,
        )
        self.session.add(user_1)
        self.session.commit()

    def get_user(
        self, users_name: str = "", users_surname: str = "", users_email: str = ""
    ) -> bool:
        """
        Args:
            users_name (str): _description_
            users_surname (str): _description_
            user_email (str): _description_

        Get user from base.
        function check user name and surname and email
            if its equal:
                user can chose to do some things: add task, edit task, delete task
            if dont equal:
                user must to register"""
        try:
            user = (
                self.session.query(User)
                .filter_by(
                    user_name=users_name,
                    user_surname=users_surname,
                    user_email=users_email,
                )
                .one()
            )

            return user.id

        # except SQLAlchemyError as e: # only for test
        except:
            return False  # [] užbaigti logiką

    def get_users(self) -> list:
        users = self.session.query(User).all()
        user_id: list = []
        print("ID")
        for user in users:
            print(user.id, user.user_name, user.user_surname, user.user_email)
            user_id.append(user.id)
        return user_id

    def delete_user(self, user_id: int):
        user = self.session.query(User).get(user_id)
        self.session.delete(user)
        self.session.commit()

    def delete_user_task(self, task_id: int):
        task = self.session.query(Task).get(task_id)
        self.session.delete(task)
        self.session.commit()

    def check_password(self, users_email: str, user_passwd: str):
        self.users_email = users_email

        try:
            by_user_email = (
                self.session.query(User).filter_by(user_email=self.users_email).first()
            )

            if by_user_email.user_passwd == user_passwd:  # type:ignore #!
                return True

        except:
            return False

    def create_task(
        self,
        user_email: str = "",
        task_name: str = "",
        task_note: str = "",
    ) -> None:
        by_user_email = (
            self.session.query(User).filter_by(user_email=user_email).first()
        )

        task = Task(
            task_name=task_name,
            task_note=task_note,
            task_id=by_user_email.id,  # type:ignore #!
        )
        user_one = self.session.query(User).get(by_user_email.id)  # type:ignore #!

        user_one.tasks.append(task)
        self.session.commit()
        print("Task created successfully !")

    def get_tasks(self, user_email: str) -> list:
        get_user = self.session.query(User).filter_by(user_email=user_email).first()
        tasks = (
            self.session.query(Task).filter_by(task_id=get_user.id).all()
        )  #! #type:ignore
        return tasks

    def change_task(
        self,
        task_id: int,
        task_name: str,
        task_note: str,
        task_finished: str,
        task_status: str,
    ):
        user_task = self.session.query(Task).get(task_id)
        user_task.task_name = task_name
        user_task.task_note = task_note
        user_task.task_finish_date = task_finished
        user_task.task_status = task_status
        self.session.commit()


database = SqliteDatabase(filename="tasks")
database.create_database()
