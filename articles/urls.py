from rest_framework.routers import DefaultRouter

from articles.views import ArticlesViewSet, UserViewSet, KeywordViewSet

router = DefaultRouter()
router.register('articles', ArticlesViewSet)
router.register('users', UserViewSet)
router.register('keywords', KeywordViewSet)

urlpatterns = router.urls
