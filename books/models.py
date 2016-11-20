from builtins import str

from django.conf import settings
from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from push_notifications.models import APNSDevice
from rest_framework.authtoken.models import Token


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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
