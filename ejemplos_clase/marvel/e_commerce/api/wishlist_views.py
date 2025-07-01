from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from e_commerce.models import WishList
from e_commerce.api.serializers import WishListSerializer


class WishListCartFavoritesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class CartAndFavoritesView(ListAPIView):
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = WishListCartFavoritesPagination

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return WishList.objects.filter(
            user_id=user_id,
            favorite=True,
            cart=True
        )
