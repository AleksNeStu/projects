import datetime

import mongoengine as me


class User(me.Document):

    # no id as in sql ver
    # NO SQL: required=False ~ SQL: nullable=True
    name: str = me.StringField(required=False)
    email: str = me.StringField(unique=True) # index=True
    hashed_password: str = me.StringField(unique=True) # index=True
    created_date: datetime.datetime = me.DateTimeField(
        default=datetime.datetime.now) # index=True
    profile_image_url: str = me.StringField()
    last_login: datetime.datetime = me.DateTimeField(
        default=datetime.datetime.now) # index=True

    meta = {
        'db_alias': 'core', # data.db_session.init_no_sql
        'collection': 'users',
        'indexes': [
            'email',
            'hashed_password',
            'created_date',
            'last_login',
        ]
    }

