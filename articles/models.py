from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256)
    abstract = models.TextField()
    content = models.TextField()
    # lista słów kluczowych, może być pusta
    keywords = models.ManyToManyField('articles.Keyword', related_name='articles', blank=False)
    # kto utworzył artykuł
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='articles', null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'


class Keyword(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# Create your models here.
