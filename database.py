from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError  # error handling
from db.base import Base
from datetime import datetime, time
from models.user import User
from models.tasks import Task


class SqliteDatabase:
    def __init__(self, filename: str = "") -> None:
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

    def get_user(self, user_email: str) -> Optional[User]:
        """
        Args:

            user_email (str): _description_

        Get user from base.
        function check is user email is unique
        """

        user = (
            self.session.query(User)
            .filter_by(
                user_email=user_email,
            )
            .one()
        )

        return user

    def get_users(self) -> list[int]:
        users = self.session.query(User).all()
        user_ids: list = []
        print("ID")
        for user in users:
            user_ids.append(user.id)
        return user_ids

    def delete_user(self, user_id: int) -> None:
        user = self.session.query(User).get(user_id)
        self.session.delete(user)
        self.session.commit()

    def delete_user_task(self, task_id: int) -> None:
        task = self.session.query(Task).get(task_id)
        self.session.delete(task)
        self.session.commit()

    def check_password(self, users_email: str, user_passwd: str) -> bool:
        self.users_email = users_email
        try:
            by_user_email = (
                self.session.query(User).filter_by(user_email=self.users_email).first()
            )
            if by_user_email.user_passwd == user_passwd:  # type:ignore #!
                return True
            else:
                return False

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

    def get_tasks_by_user(self, user_email: str) -> list:
        get_user = self.session.query(User).filter_by(user_email=user_email).first()
        tasks = (
            self.session.query(Task).filter_by(task_id=get_user.id).all()
        )  #! #type:ignore
        tasks_id: list = []
        for n in get_user.tasks:  # type:ignore
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
        return tasks_id

    def change_task(
        self,
        task_id: int,
        task_name: str,
        task_note: str,
        task_finished: datetime,
        task_status: str,
    ) -> None:
        user_task = self.session.query(Task).get(task_id)
        user_task.task_name = task_name
        user_task.task_note = task_note
        user_task.task_finish_date = task_finished
        user_task.task_status = task_status
        self.session.commit()


database = SqliteDatabase(filename="tasks")
database.create_database()
