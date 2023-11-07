import datetime

import mongoengine as me


class Audit(me.Document):

    id = me.StringField(primary_key=True)
    created_date = me.DateTimeField(default=datetime.datetime.now)
    description = me.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'audit',
        'indexes': [
            'created_date',
        ]
    }
