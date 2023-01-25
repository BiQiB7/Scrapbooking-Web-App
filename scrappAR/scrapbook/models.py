from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Posts(models.Model):
	created_on = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	image = models.ManyToManyField('Image', blank=True, null=True)
	# photo = models.ImageField(upload_to='scrapbook/post_pics', blank=True, null=True, default = 'blank.png')

class Image(models.Model):
	image = models.ImageField(upload_to='media/', blank=True, null=True, default = 'blank.png')

class Comment(models.Model):
	comment = models.TextField()
	created_on = models.DateTimeField(timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Posts', on_delete=models.CASCADE)


class Likes(models.Model):
    like = models.IntegerField()