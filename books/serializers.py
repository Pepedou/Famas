from django.db.models import Q
from push_notifications.models import APNSDevice
from rest_framework import serializers

from books.models import BookPage


class BookPageSerializer(serializers.HyperlinkedModelSerializer):
    """
    BookPage model serializer for the rest api framework.
    """

    class Meta:
        model = BookPage
        fields = ('id', 'page_number', 'title', 'image', 'content')

    def update(self, instance, validated_data):
        instance = super(BookPageSerializer, self).update(instance, validated_data)

        for device in APNSDevice.objects.exclude(Q(name='iPhone 5S MMG') | Q(active=False)):
            device.send_message('La protagonista ha completado la página "{0}".'.format(
                instance.title
            ), badge=1, sound='NotificationSound.wav')

        return instance
