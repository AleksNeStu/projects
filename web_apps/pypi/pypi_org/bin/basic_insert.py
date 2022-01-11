import settings
from data import db_session


def init_db():
    db_session.global_init(settings.DB_CONNECTION)


def main():
    init_db()


if __name__ == '__main__':
    main()