from builtins import str

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class BookPage(models.Model):
    """
    The page of a book. It consists of a title, an image and its content.
    """
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/')
    content = models.CharField(max_length=1024, default="")

    def __str__(self):
        return str(self.title)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(instance=None, created=False):
    if created:
        Token.objects.create(user=instance)
