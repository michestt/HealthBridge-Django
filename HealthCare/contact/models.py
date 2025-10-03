from django.db import models
# Create your models here.


class message_subject_1(models.Model):
	subject = [
		['blog', 'I have a problem about my post'],
		['yoga', 'My yoga video is not working'],
		['other', 'Other'],
	]
	title = models.CharField(max_length=250, blank=False)
	description = models.CharField(max_length=250, blank=True, null=True)

	def __str__(self):
		return self.title


class message_subject_2(models.Model):
	category = models.ForeignKey(message_subject_1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250, blank=False)
	description = models.CharField(max_length=250, blank=True, null=True)

	def __str__(self):
		return self.title


class Contact(models.Model):
	user_name = models.CharField(max_length=50, default="(No Name)")
	message_subject2 = models.ForeignKey(message_subject_2, null=True, on_delete=models.SET_DEFAULT, default=6)
	user_email = models.CharField(max_length=50)
	user_message = models.CharField(max_length=100)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.user_name
