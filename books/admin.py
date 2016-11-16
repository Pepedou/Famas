from django.contrib import admin
from push_notifications.models import APNSDevice

from books import models
from books.forms.book_forms import BookPageForm


class BookPageModelAdmin(admin.ModelAdmin):
    """
    Admin to describe a BookPage.
    """
    form = BookPageForm
    actions = ['send_push_notification']

    def send_push_notification(self, request, queryset):
        """
        Admin action to send a notification about the selected book
        pages.
        :param request: HTTPRequest
        :param queryset: The book pages.
        """
        devices = APNSDevice.objects.filter(active=True)

        if queryset.count() == 1:
            message = 'Una nueva página ha llegado de otra dimensión: "{0}"'.format(queryset[0].title)
        else:
            message = '{0} páginas han llegado de otra dimensión: {1}'.format(
                queryset.count(), ', '.join([x.title for x in queryset.order_by('page_number')]))

        devices.send_message(message, badge=queryset.count(), sound='NotificationSound.wav')

        self.message_user(request, message)

    send_push_notification.short_description = 'Send push notifications'


admin.site.register(models.BookPage, BookPageModelAdmin)
