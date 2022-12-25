# For app.autodiscover_tasks() to work as described, you need to define your Celery tasks in a separate tasks.py module inside of each app of your Django project.
from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(3)  # Simulate expensive operation that freezes Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email_address],
        fail_silently=False,
    )
