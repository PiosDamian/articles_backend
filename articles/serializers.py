from rest_framework import serializers

from articles.models import Article, User, Keyword
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'firstname', 'lastname', 'password', 'articles', 'number_of_articles']

    number_of_articles = serializers.SerializerMethodField()

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    def get_number_of_articles(self, instance):
        return instance.get_number_of_articles()

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
