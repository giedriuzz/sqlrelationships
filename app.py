from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
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

    def get_user(self):
        pass


database = SqliteDatabase(filename="tasks_new.db")
database.create_database()

database.register_user(
    user_name="Giedrius",
    user_surname="Kuprys",
    user_email="giedrius@gmail.com",
    user_passwd="123",
)
