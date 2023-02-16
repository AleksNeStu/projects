from django.contrib import admin

import notes
from . import models
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created') # display http://localhost:8000/admin/notes/notes/
    list_filter = ()
    # save_as = True


admin.site.register(models.Notes, NotesAdmin)