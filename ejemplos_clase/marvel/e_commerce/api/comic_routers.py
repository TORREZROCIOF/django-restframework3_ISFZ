from rest_framework.routers import DefaultRouter
from .comic_viewsets import ComicListOnlyViewSet

router = DefaultRouter()

router.register(r'comics-filtered', ComicListOnlyViewSet, basename='comics-filtered')

urlpatterns = router.urls
