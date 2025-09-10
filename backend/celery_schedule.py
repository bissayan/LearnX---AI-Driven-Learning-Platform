from celery.schedules import crontab
from flask import current_app as app

from backend.tasks import  send_assignment_deadline_reminder
celery_app = app.extensions['celery']


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Sets up periodic tasks for Celery Beat.
    """
    sender.add_periodic_task(crontab(minute='*/5'), send_assignment_deadline_reminder.s(), name='Send assignment reminder')

    

