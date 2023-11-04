import datetime

import mongoengine as me


class Release(me.Document):
    package_id = me.StringField()

    major_ver = me.IntField()
    minor_ver = me.IntField()
    build_ver = me.IntField()

    created_date = me.DateTimeField(default=datetime.datetime.now)
    comment = me.StringField()
    url = me.StringField()
    size = me.IntField()

    meta = {
        'db_alias': 'core',
        'collection': 'releases',
        'indexes': [
            'created_date',
            'package_id',
            'major_ver',
            'minor_ver',
            'build_ver',
            {'fields': ['major_ver', 'minor_ver', 'build_ver']},
            {'fields': ['-major_ver', '-minor_ver', '-build_ver']},
        ]
    }

    @property
    def version_text(self):
        return '{}.{}.{}'.format(
            self.major_ver, self.minor_ver, self.build_ver)
