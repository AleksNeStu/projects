import sqlalchemy as sa
import sqlalchemy.orm as orm

factory = None

def global_init(conn_str: str):
    global factory
    if factory:
        return

    # engine
    engine = sa.create_engine(conn_str, echo=True)
    # session
    factory = orm.sessionmaker(bind=engine)



