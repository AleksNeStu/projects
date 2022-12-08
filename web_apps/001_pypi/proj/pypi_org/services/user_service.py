import logging
from typing import Optional, Union

import bson

import app
from utils import sec as sec_utils

if app.is_sql_ver:
    import sqlalchemy.orm as orm
    from data import db_session
    from data.models.users import User

    def get_users() -> orm.Query:
        with db_session.create_session() as session:
            return session.query(User)


    def get_user(email: str, password: str = None,
                 users: orm.Query = None) -> Optional[User]:
        users = users or get_users()
        user = users.filter(User.email == email).first()
        if (password and
                user and
                not sec_utils.is_pass_hash_correct(
                    user.hashed_password, password)):
            return

        users.session.close()
        return user


    def get_user_by_id(user_id: Union[int, None],
                       users: orm.Query = None) -> Optional[User]:
        users = users or get_users()
        user = users.filter(User.id == user_id).first()
        users.session.close()

        return user


    def create_user(name: str, email: str, password: str) -> Optional[User]:
        if get_user(email=email):
            return

        with db_session.create_session() as session:
            pass_hash = sec_utils.pass_to_hash(password)
            user = User(
                name=name,
                email=email,
                hashed_password=pass_hash
            )
            session.add(user)
            session.commit()

        return user

else:
    from mongoengine import QuerySet
    import mongoengine as me
    from data.models_no_sql.users import User

    def get_users() -> QuerySet:
        return User.objects()


    def get_user(email: str, password: str = None,
                 users: QuerySet = None) -> Optional[User]:
        users = users or get_users()
        user = users.filter(email=email).first()
        if (password and
                user and
                not sec_utils.is_pass_hash_correct(
                    user.hashed_password, password)):
            return

        return user


    def get_user_by_id(user_id: Union[bson.ObjectId, None],
                       users: QuerySet = None) -> Optional[User]:
        users = users or get_users()
        # mongoengine.errors.ValidationError: '0' is not a valid ObjectId,
        # it must be a 12-byte input or a 24-character hex string
        try:
            return users.filter(id=user_id).first()

        except (me.errors.ValidationError, ) as err:
            logging.warning(f"No user for auth via no sql version: {err}")
            return


    def create_user(name: str, email: str, password: str) -> Optional[User]:
        if get_user(email=email):
            return

        pass_hash = sec_utils.pass_to_hash(password)
        user = User(
            name=name,
            email=email,
            hashed_password=pass_hash
        )
        user.save()

        return user