import datetime

import mongoengine as me


class Package(me.Document):
    id = me.StringField(primary_key=True)
    created_date = me.DateTimeField(default=datetime.datetime.now)
    last_updated_date = me.DateTimeField(default=datetime.datetime.now)
    summary = me.StringField()
    description = me.StringField()

    home_page = me.StringField()
    docs_url = me.StringField()
    package_url = me.StringField()

    author = me.StringField()
    author_email = me.StringField()
    license = me.StringField()

    # pypi_org/data/models/maintainers.py
    # normalization table for many-to-many relationship
    maintainers = me.ListField(me.ObjectIdField())

    meta = {
        'db_alias': 'core',
        'collection': 'packages',
        'indexes': [
            'created_date',
            'last_updated_date',
            'author_email',
            'license',
        ]
    }

    def __repr__(self):
        return '<Package {}>'.format(self.id)
