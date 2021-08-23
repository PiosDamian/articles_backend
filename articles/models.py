from django.db import models


class User(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
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
    author = models.ForeignKey('articles.User', on_delete=models.SET_NULL, related_name='articles', null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'


class Keyword(models.Model):
    name = models.CharField(max_length=64)
    articles = models.ManyToManyField('articles.Article', related_name='keywords', blank=True)

    def __str__(self):
        return self.name

# Create your models here.
