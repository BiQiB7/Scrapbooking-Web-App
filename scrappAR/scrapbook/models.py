from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Topic(models.Model):
    name = models.CharField(max_length = 200, blank = True)
    
    def __str__(self):
        return self.name
class Image(models.Model):
	image = models.ImageField(upload_to='media/', blank=True, null=True, default = 'blank.png')
	
class Scrapbook(models.Model):
	title = models.CharField(max_length = 200)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, blank = True, null=True)
	# cover = models.ImageField('Image',blank=True, null=True)
	cover = models.ImageField(Image,upload_to='media/', blank=True, null=True, default = 'blank.png')
	def set_cover(self, cover):
		self.cover = cover
		self.save()
	def __str__(self):
		return self.title
	

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






class Comment(models.Model):
	comment = models.TextField()
	created_on = models.DateTimeField(timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Posts', on_delete=models.CASCADE)


class Likes(models.Model):
    like = models.IntegerField()

