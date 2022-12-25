from .celery import app as celery_app

# To make sure that your Celery app is loaded when you start Django, you should add it to __all__
# Loading the Celery app on Django startup ensures that the @shared_task decorator will use it correctly.
__all__ = ("celery_app",)
