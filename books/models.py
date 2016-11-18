import os
from builtins import str

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from rest_framework.authtoken.models import Token
from sendgrid import Email, sendgrid
from sendgrid.helpers.mail import Content
from sendgrid.helpers.mail import Mail


def get_next_page_number():
    """
    Returns the following number after the maximum page number registered.
    :return: An integer.
    """
    max_page_number = BookPage.objects.aggregate(Max('page_number'))['page_number__max']

    if max_page_number is None:
        return 0
    else:
        return max_page_number + 1


class BookPage(models.Model):
    """
    The page of a book. It consists of a title, an image and its content.
    """
    page_number = models.PositiveSmallIntegerField(default=get_next_page_number, unique=True)
    title = models.CharField(max_length=13, default="")
    image = models.ImageField(upload_to='images/')
    content = models.TextField(default="")

    def __str__(self):
        return str(self.title)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        book_page = super(BookPage, self).save(force_insert, force_update, using, update_fields)

        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("codificadoramexico@gmail.com")
        subject = "Hello World from the SendGrid Python Library!"
        to_email = Email("pepedou@gmail.com")
        content = Content("text/plain", "Hello, Email!")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())

        print(str(response))

        return book_page


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
