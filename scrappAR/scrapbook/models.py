from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class Topic(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Scrapbook(models.Model):
	name = models.CharField(max_length = 200)
	# posts = Posts.objects.all()
	def __str__(self):
		return self.name

class select_scrapbook(models.Model):
	scrapbook = models.CharField(max_length=100)
	class Meta:
		db_table = 'scrapbooks'

class Posts(models.Model):
	created_on = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	image = models.ManyToManyField('Image', blank=True, null=True)
	scrapbook = models.ForeignKey(Scrapbook, on_delete=models.CASCADE, null= True)
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

