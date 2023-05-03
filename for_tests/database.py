from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker


class SqliteDatabase:
    def __init__(self, filename: str, base) -> None:
        self.filename = filename
        self.base = base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        self.session = sessionmaker(bind=self.engine)

    def create_database(self):
        self.base.metadata.create_all(self.engine, checkfirst=True)

    def create_object(self, object: DeclarativeMeta):
        pass
