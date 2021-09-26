from rest_framework.viewsets import ModelViewSet

from articles.models import Article, Keyword
from articles.serializers import ArticleSerializer, KeywordsSerializer


class ArticlesViewSet(ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filterset_fields = ('keywords',)


class KeywordViewSet(ModelViewSet):
	queryset = Keyword.objects.all()
	serializer_class = KeywordsSerializer
