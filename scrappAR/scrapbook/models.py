from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Post(models.Model):
    
	# photo = models.ImageField(upload_to='users/%Y/%m/%d', blank = True)
        #upload_to = 'scrapbook/post_pics',
        #blank = True,
        #null = True
    #)
	
	#created_on = models.DateTimeField(default=timezone.now)
	#author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()


class Comment(models.Model):
	comment = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Likes(models.Model):
    like = models.IntegerField()