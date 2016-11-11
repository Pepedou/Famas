from rest_framework import viewsets

from books.models import BookPage
from books.serializers import BookPageSerializer


class BookPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BookPages to be viewed or edited.
    """
    queryset = BookPage.objects.order_by('page_number')
    serializer_class = BookPageSerializer
