# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#writing-custom-template-filters
from django.template.defaulttags import register


@register.filter
def get_val(dictionary, key):
    return dictionary.get(key)

# If file is empty it will raise and error:
# http://localhost:8000/notes/notesv1
'''
TemplateSyntaxError at /notes/notesv1
'poll_extras' is not a registered tag library. Must be one of:
admin_list
admin_modify
admin_urls
cache
django_browser_reload
i18n
l10n
log
static
tz
'''