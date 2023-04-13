from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Image(models.Model):
   followers = models.IntegerField(default = 0)
   desc = models.CharField(max_length=200, null = True)
   job = models.CharField(max_length=200, null = True)
   caption=models.CharField(max_length=100, null = True)
   image=models.ImageField(upload_to="img/%y", null = True)
   pic=models.ImageField(upload_to="img/%y", default = "blank.png")
   following = models.IntegerField(default = 0)
   
   
   def __str__(self):
    return self.caption
