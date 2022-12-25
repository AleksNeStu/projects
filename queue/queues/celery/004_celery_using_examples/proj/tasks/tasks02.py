from __future__ import absolute_import, unicode_literals

import os
from io import StringIO

from celery import shared_task
from celery.schedules import crontab
# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
from django.conf import settings
from django.core.mail import mail_admins, EmailMessage

from .models import IntervalCheckpoint



from .models import CheckpointFile


# from celery_uncovered.toyex.tasks import report_error_task, register_error_for_admin
"""
Scenario 2 - Report on Server 500 Errors via Email
One of the most common use cases for Celery is sending email notifications. Email notification is an offline I/O bound operation that leverages either a local SMTP server or a third-party SES. There are many use cases that involve sending an email and, for most of them, the user doesn’t need to wait until this process is finished before receiving an HTTP response. That’s why it is preferred to execute such tasks in the background and respond to the user immediately.


I) Desc:
Create a logging handler that will be able to track Server errors (50X) and report them to admins through via celery.
I advice to thoroughly understand https://docs.djangoproject.com/en/1.11/howto/error-reporting/

Seems like you need to extend default  'django.utils.log.AdminEmailHandler',

II) Implementation Details:
1. Create self containable task called `report_error_task/4 similar to `self.send_mail(subject, message,
fail_silently=True, html_message=html_message)``
2. Extend 'django.utils.log.AdminEmailHandler' in the way it will call report_error_task.delay with the
required parameters
3. Return nothing (Ensure that ignore_result flag set to True)
4. Provide http tests that ensures that it is called

III) Extra:
1. Modify code so that task could be scheduled once per time range (1 hour, 6 hours) and all bugs will be collected and
send as one email, rather than notifying often.
Hint: you also need to create models.py that will store the HttpErrorEntries

IV) Required Libraries:
    django.core.mail
    django.util.log
    mailhog
    pytest
"""
@shared_task
def report_error_task(subject, message, *args, **kwargs):
    mail_admins(subject, message, *args, **kwargs)


@shared_task
def register_error_for_admin(subject, message, *args, **kwargs):
    """Registers error by storing result to a file"""
    chk_file = CheckpointFile.error_file(subject)
    chk_file.write(message)


# @periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
@shared_task
def report_scheduled_error_task():
    errors_content = StringIO()
    at_least_one_flag = False
    for chk_file in CheckpointFile.read_relevant_error_files():
        header_text = "--" * 10 + " %s " % chk_file.filename + "--" * 10
        # head
        errors_content.write(header_text)
        errors_content.write(os.linesep)
        # body
        errors_content.write(chk_file.read())
        # tail
        errors_content.write(os.linesep * 5)
        at_least_one_flag = True

    if not at_least_one_flag:
        return

    email = EmailMessage(
        subject="Error report",
        body="Scheduled error report for admin",
        from_email=settings.SERVER_EMAIL,
        to=[a[1] for a in settings.ADMINS])
    email.content_subtype = "html"
    email.attach("error_dump.log", errors_content.getvalue(), 'text/plain')
    email.send()

    error_dir = '{media}/errors/'.format(media=settings.MEDIA_ROOT)
    IntervalCheckpoint.update_current(error_dir)