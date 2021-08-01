from django.db import models


class User(models.Model):
    login = models.CharField(max_length=128, min_length=3)
    password = models.CharField(min_length=5)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.login}: {self.firstname} {self.lastname}'

    def get_number_of_articles(self):
        return self.articles.all().count()


class Article(models.Model):
    title = models.CharField(max_length=256)
    abstract = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='articles')

    def __str__(self):
        return f'{self.title} - {self.author}'


class Keyword(models.Model):
    name = models.CharField(max_length=64)
    articles = models.ManyToManyField(Article, related_name='keywords')

    def __str__(self):
        return self.name

# Create your models here.
