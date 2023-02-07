from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Image(models.Model):
   caption=models.CharField(max_length=100)
   image=models.ImageField(upload_to="img/%y")
   
   
   
   def __str__(self):
    return self.caption 
