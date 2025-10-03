from django.db import models

# Create your models here.

class Level(models.Model):
	status = models.CharField(max_length=50,null=False)
	def __str__(self):
		return self.status

class Post(models.Model):
	level=models.ForeignKey('Level', on_delete=models.CASCADE)
	nickname=models.CharField(max_length=100,default='People who are unwilling to reveal their identity')
	byear = models.CharField(max_length=4, default=1960)
	message=models.TextField(null=False)
	del_pass=models.CharField(max_length=10, blank=True)
	pub_time=models.DateTimeField(auto_now=True)
	enabled=models.BooleanField(default=True)

	def __str__(self):
		return self.message

