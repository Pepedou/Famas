from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest
from push_notifications.models import APNSDevice
from rest_framework import viewsets

from books.models import BookPage
from books.serializers import BookPageSerializer


class BookPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BookPages to be viewed or edited.
    """
    queryset = BookPage.objects.order_by('page_number')
    serializer_class = BookPageSerializer


def register_device_token(request, token):
    """
    Adds a new APNS device with the token as the registration ID.
    :param request: HTTPRequest
    :param token: Device Token
    :return: HTTPResponse
    """
    try:
        device = APNSDevice(registration_id=token)
        device.save()
    except IntegrityError:
        return HttpResponseBadRequest()

    return HttpResponse(device.registration_id)
