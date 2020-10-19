from rest_framework.routers import DefaultRouter

from comment.views import CommentViewSet, ReviewViewSet
from users.views import UserViewSet
from .views import CategoriesViewSet, GenresViewSet, TitleViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet, basename='comment')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
