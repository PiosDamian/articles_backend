import pytest

from articles.tests.factories import UserFactory, ArticleFactory


@pytest.mark.django_db
def test_article_str():
    article = ArticleFactory(title='test')
    assert str(article).startswith('test - ')


@pytest.mark.django_db
def test_author_number_of_articles():
    author = UserFactory()
    ArticleFactory(author=author)
    assert author.get_number_of_articles() == 1
