import pytest
from rest_framework import status

from articles.tests.factories import ArticleFactory


@pytest.mark.django_db
def test_articles_list(client):
	ArticleFactory()
	response = client.get('/api/v1/articles/articles/')
	assert response.status_code == status.HTTP_200_OK
	assert len(response.data) == 1


def test_articles_list_unauthorized(unauthorized_client):
	response = unauthorized_client.get('/api/v1/articles/articles/')
	assert response.status_code == status.HTTP_401_UNAUTHORIZED
