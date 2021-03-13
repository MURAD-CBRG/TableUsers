import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

DataBase = sqlalchemy.ext.declarative.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    prop_base = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    engine = sqlalchemy.create_engine(prop_base, echo=False)
    __factory = sqlalchemy.orm.sessionmaker(bind=engine)

    from . import __all_models

    DataBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()
