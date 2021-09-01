from rest_framework.viewsets import ModelViewSet

from articles.models import Article, Keyword, User
from articles.serializers import ArticleSerializer, UserSerializer, KeywordsSerializer


class ArticlesViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ('keywords',)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KeywordViewSet(ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordsSerializer
