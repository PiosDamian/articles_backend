from rest_framework import serializers

from articles.models import Article, Keyword
from users.models import UserSerializer


class KeywordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Keyword
		fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
	keywords = KeywordsSerializer(read_only=False, many=True)
	author = UserSerializer(required=False)

	class Meta:
		model = Article
		fields = ('id', 'title', 'abstract', 'content', 'author', 'keywords')

	def create(self, validated_data):
		# tworzenie pustego artykułu w bazie
		article = Article.objects.create()
		try:
			article.title = validated_data.get('title')
			article.abstract = validated_data.get('abstract')
			article.content = validated_data.get('content')
			article.author = self.context['request'].user
			article.keywords.set(map(lambda el: el['id'], self.context['request'].data['keywords']))
			# artykuł już w bazie istnieje, należy zapisać zmiany
			article.save()
			return article
		except Exception as e:
			print(e)
			# obiekt w bazie został utworzony, ale nie został zaktualizowany - metoda save
			# jeżeli wystąpi wyjątek artykuł należy usunąć
			article.delete()
			return None
