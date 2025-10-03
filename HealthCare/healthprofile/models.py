from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

Country= (
	("UK","United Kingdom of Great Britain and Northern Ireland"),
	("CA","CANADA"),
	("AU","AUSTRALIA"),
	("FR","FRANCE"),
	("US","UNITED STATES"),
	("HK","HONG KONG"),
	("KR","KOREA, REPUBLIC OF"),
	("DE","GERMANY, FEDERAL REPUBLIC OF GERMANY"),
	("CH","SWITZERLAND"),
	("RU","Russian Federation"),
	("IL","ISRAEL"),
	("NZ","New Zealand"),
	("IT","ITALY"),
	("MY","Malaysia"),
	("SG","Singapore"),
	("SE","SWEDEN"),
	("IN","INDIA"),
	("FI","FINLAND"),
	("CN","CHINA"),
	("TW","TAIWAN,REPUBLIC OF CHINA"),
	('NA','OTHER'),
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
	profile_picture = models.ImageField(upload_to='users_profile', null=True, blank=True, default='user_default.png')
	country = models.CharField(choices=Country, default="TW", max_length=50)
	gender = models.BooleanField(default=True)
	BOD = models.DateField(null=True)
	self_introduction = models.TextField(default='', blank=True)
	expertise = models.TextField(blank=True)
	upload_date = models.DateField(auto_now=True, blank=True)

	def __str__(self):
		return self.user.username


class Contact(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = PhoneNumberField(blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	website = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.user.username
