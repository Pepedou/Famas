from builtins import str
from django.db import models


class BookPage(models.Model):
    """
    The page of a book. It consists of a title, an image and its content.
    """
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/')
    content = models.CharField(max_length=1024, default="")

    def __str__(self):
        return str(self.title)
