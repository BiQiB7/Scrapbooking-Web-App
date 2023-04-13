from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Image(models.Model):
   followers = models.IntegerField(default = 0)
   desc = models.CharField(max_length=200, null = True)
<<<<<<< HEAD
   job = models.CharField(max_length=200, null = True)
=======
   name = models.CharField(max_length=200, null = True)
>>>>>>> 4f52aba3eba81411cb7fd24db08a7c0af82c98b0
   caption=models.CharField(max_length=100, null = True)
   image=models.ImageField(upload_to="img/%y", null = True)
   pic=models.ImageField(upload_to="img/%y", default = "blank.png")
   following = models.IntegerField(default = 0)
   
   
   def __str__(self):
    return self.caption
