from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
	def create_user(self, email, password, **kwargs):
		user = self.model(email=email, **kwargs)
		user.set_password(password)
		user.is_active = True
		user.save()
		return user

	def create_superuser(self, email, password, **kwargs):
		return self.create_user(email, password, is_superuser=True, **kwargs)


class User(AbstractBaseUser):
	email = models.EmailField('Email', unique=True)
	first_name = models.CharField('Imię', max_length=128)
	last_name = models.CharField('Nazwisko', max_length=128)
	is_active = models.BooleanField('Czy aktywny?', default=False)
	is_superuser = models.BooleanField('Czy admin?', default=False)

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = UserManager()
