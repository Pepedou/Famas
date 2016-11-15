from django.contrib import admin

from books import models
from books.forms.book_forms import BookPageForm


class BookPageModelAdmin(admin.ModelAdmin):
    """
    Admin to describe a BookPage.
    """
    form = BookPageForm


admin.site.register(models.BookPage, BookPageModelAdmin)
