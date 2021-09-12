import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


@pytest.fixture
def unauthorized_client():
	return APIClient()


@pytest.fixture
def client():
	user = User.objects.create(
		email='john.doe@exmaple.com',
		first_name='John',
		last_name='Doe',
		is_active=True
	)
	refresh = RefreshToken.for_user(user)
	api_client = APIClient()
	api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
	api_client.user = user
	return api_client
