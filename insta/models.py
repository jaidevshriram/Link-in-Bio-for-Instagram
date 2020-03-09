from django.db import models
from django.contrib.auth.models import User

class Social(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

class Post(models.Model):
	link = models.URLField()
	img = models.ImageField(upload_to='posts/')
	title = models.TextField()
	info = models.TextField(blank=True)

	def __str__(self):
		return self.title