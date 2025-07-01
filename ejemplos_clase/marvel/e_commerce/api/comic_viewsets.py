from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from e_commerce.models import Comic
from e_commerce.api.serializers import ComicSerializer


class ComicListOnlyViewSet(ModelViewSet):
    serializer_class = ComicSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comic.objects.filter(stock_qty__gte=5)

    http_method_names = ['get'] 

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'marvel_id']
    search_fields = ['title'] 
    ordering_fields = ['marvel_id', 'title']
    ordering = ['-marvel_id'] 
