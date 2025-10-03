from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, Contact


def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		Contact.objects.create(user=instance)
		print("profile created")


post_save.connect(create_profile, sender=User)

