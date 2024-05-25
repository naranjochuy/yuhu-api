from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task
def send_email_task():
    subject = "Yuhu"
    message = "Detection of changes in tasks"
    email_sender = settings.EMAIL_HOST_USER
    destination_emails = settings.EMAIL_TO_SEND
    send_mail(subject, message, email_sender, destination_emails)
    return True
