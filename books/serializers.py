from rest_framework import serializers

from books.models import BookPage


class BookPageSerializer(serializers.HyperlinkedModelSerializer):
    """
    BookPage model serializer for the rest api framework.
    """

    class Meta:
        model = BookPage
        fields = ('title', 'image', 'content')
