from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError  # error handling
from db.base import Base
from models.user import User
from models.tasks import Task


class SqliteDatabase:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        # self.base = base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_database(self):  # [x]
        Base.metadata.create_all(self.engine, checkfirst=True)

    def create_object(self, object: DeclarativeMeta):
        pass

    def register_user(
        self, user_name: str, user_surname: str, user_email: str, user_passwd: str
    ):  # [x]
        """_summary_

        Args:
            user_name (str): _description_
            user_surname (str): _description_
            user_email (str): _description_
            user_passwd (str): _description_
        """ """"""
        self.user_name = user_name
        self.user_surname = user_surname
        self.user_email = user_email
        self.user_passwd = user_passwd

        user_1 = User(
            user_name=self.user_name,
            user_surname=self.user_surname,
            user_email=self.user_email,
            user_passwd=self.user_passwd,
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

    def get_password(self, user_passwd: str):
        try:
            print(self.get_user())
            user = self.session.query(User).get(self.get_user())
            print(user)
            print(user.user_passwd)
            if user.user_passwd == user_passwd:
                print("passwd OK")
        except:
            print("passwd NOT OK")


database = SqliteDatabase(filename="tasks_new.db")
database.create_database()

# database.register_user(
#     user_name="Giedrius",
#     user_surname="Kuprys",
#     user_email="giedrius@gmail.com",
#     user_passwd="123",
# )


print(
    database.get_user(
        users_name="Giedrius", users_surname="Kuprys", users_email="giedrius@gmail.com"
    )
)
database.get_password(user_passwd="123")
