from django.db import models

# Create your models here.
class Contact(models.Model):
	fullname = models.CharField(max_length=30)
	subject = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Users(models.Model):

	class AccountType(models.TextChoices):
		FREE = 'FR'
		SILVER = 'SL'
		GOLD = 'GL'
		PLATINUM = 'PL'

	COUNTRY_CODE = [
		('AR', 'Argentina'),
		('BR', 'Brasil'),
		('CH', 'Chile'),
		('ES', 'España'),
		('PE', 'Perú')
	]


	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	account_type = models.CharField(max_length=2,choices=AccountType.choices,default=AccountType.FREE)
	country = models.CharField(max_length=2,choices=COUNTRY_CODE,default='PE')
	enabled = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
