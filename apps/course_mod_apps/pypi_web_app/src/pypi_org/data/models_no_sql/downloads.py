import datetime

import mongoengine as me


class Download(me.Document):
    created_date = me.DateTimeField(default=datetime.datetime.now)

    package_id = me.StringField()
    release_id = me.IntField()

    ip_address = me.StringField()
    user_agent = me.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'documents',
        'indexes': [
            'created_date',
            'package_id',
            'release_id',
        ]
    }
