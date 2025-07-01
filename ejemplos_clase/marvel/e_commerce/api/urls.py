from django.urls import path, include

from e_commerce.api.marvel_api_views import *
# Importamos las API_VIEWS:
from e_commerce.api.api_views import *

from e_commerce.api.wishlist_views import CartAndFavoritesView

urlpatterns = [
    # User APIs:
    path('user/login/', LoginUserAPIView.as_view()),

    # APIs de Marvel
    path('get_comics/',get_comics),
    path('purchased_item/',purchased_item),
    
    # Comic API View:
    path('comics/get', GetComicAPIView.as_view()),
    path('comics/<int:pk>/get', GetOneComicAPIView.as_view()),
    path('comics/post', PostComicAPIView.as_view()),
    path('comics/get-post', ListCreateComicAPIView.as_view()),
    path('comics/<int:pk>/update', RetrieveUpdateComicAPIView.as_view()),
    path('comics/<int:pk>/delete', DestroyComicAPIView.as_view()),

    # TODO: Wish-list API View
    path('wish/get', GetWishListAPIView.as_view()),
    path('wish/post', PostWishListAPIView.as_view()),
    path('favs/<str:username>/get', GetUserFavsAPIView.as_view()),

    # User API Viewsets:
    path('api/', include('e_commerce.api.routers')),
    
    # Viewset solo lectura de comics
    path('api/', include('e_commerce.api.comic_routers')),
    
    path('wishlist/<int:pk>/cart-favs/', CartAndFavoritesView.as_view(), name='wishlist-cart-favs'),
]