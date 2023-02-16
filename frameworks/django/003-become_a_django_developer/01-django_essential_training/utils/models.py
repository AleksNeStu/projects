from datetime import datetime

import manage
# dj = manage.main()
# or
dj2 =  manage.init()

from notes.models import Notes
note = Notes.objects.get(pk='1')
t = note.title
# %history
txt = note.text
# all_n = Notes.objects.get_all()
all_obj = Notes.objects.all()

new_note1 = Notes.objects.get(title='n_2', text='txt2')
new_note2 = Notes.objects.create(title='n_3', text='txt3', updated=datetime.now())
all_n2 = Notes.objects.all()
filt = Notes.objects.filter(title__startswith='n_')
ex = Notes.objects.exclude(title__icontains='n_')
# %history