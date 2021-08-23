import factory.fuzzy

from articles.models import Article, User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    login = factory.fuzzy.FuzzyText()
    password = factory.fuzzy.FuzzyText()
    firstname = factory.fuzzy.FuzzyText()
    lastname = factory.fuzzy.FuzzyText()


class ArticleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.fuzzy.FuzzyText()
    abstract = factory.fuzzy.FuzzyText()
    content = factory.fuzzy.FuzzyText()
    author = factory.SubFactory(UserFactory)
