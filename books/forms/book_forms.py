from django.forms import ModelForm, BooleanField
from push_notifications.models import APNSDevice

from books.models import BookPage


class BookPageForm(ModelForm):
    """
    Form for a book page model.
    """
    send_push_notification = BooleanField(initial=False, required=False)

    class Meta:
        model = BookPage
        fields = '__all__'

    def save(self, commit=True):
        book = super(BookPageForm, self).save(commit)
        send_push_notification = self.cleaned_data.get('send_push_notification', False)

        if send_push_notification:
            for device in APNSDevice.objects.filter(active=True):
                device.send_message('Una nueva página ha llegado de otra dimensión: Página {0} - "{1}"'
                                    .format(book.page_number + 1, book.title),
                                    badge=book.page_number + 1, sound='NotificationSound.wav')

        return book
