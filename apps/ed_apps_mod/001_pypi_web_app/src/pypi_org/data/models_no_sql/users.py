import datetime

import mongoengine as me

# Example:
'''
/* 1 */
{
    "_id" : ObjectId("62128fa4d987227014ca128c"),
    "name" : "user1",
    "email" : "user1@gmail.com",
    "hashed_password" : "$6$rounds=177187$5sb7z.vqQL9tRnrv$FO.wu6embgsU7/b..jaL/adkUL4kQUXGogI7aZL2egXxvOTUXDL..6YelCjORITb9ftUpmiqyOJJLLpe/bgTI1",
    "created_date" : ISODate("2022-02-20T19:59:48.200Z"),
    "last_login" : ISODate("2022-02-20T19:59:48.200Z")
}

/* 2 */
{
    "_id" : ObjectId("62153299c1c75e0e75375d05"),
    "name" : "user2@gmail.com",
    "email" : "user2@gmail.com",
    "hashed_password" : "$6$rounds=177187$j82LJFToMGfA76eo$r2w30g58qZt1j3OWlWhd7dQJiqcCsulSMhmc6DSOdYk7gCmo.YVvl00V.gdJxXbSMfGVloR4iJyJ/F2gxRC410",
    "created_date" : ISODate("2022-02-22T19:59:37.030Z"),
    "last_login" : ISODate("2022-02-22T19:59:37.030Z")
}
'''

class User(me.Document):

    # no id as in sql ver
    # NO SQL: required=False ~ SQL: nullable=True
    # e.g. 62128fa4d987227014ca128c
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

