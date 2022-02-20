import datetime

import mongoengine as me


class License(me.Document):
    id = me.StringField(primary_key=True)
    created_date = me.DateTimeField(default=datetime.datetime.now)
    description = me.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'licenses',
        'indexes': [
            'created_date',
        ]
    }
