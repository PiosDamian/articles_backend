from rest_framework.routers import DefaultRouter

from articles.views import ArticlesViewSet, KeywordViewSet

router = DefaultRouter()
router.register('articles', ArticlesViewSet)
router.register('keywords', KeywordViewSet)

urlpatterns = router.urls
