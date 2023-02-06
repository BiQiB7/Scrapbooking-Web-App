from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
# Create your models here.
User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(default = 1)
    bio = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'blank-user.jpg' )
    location = models.CharField(max_length = 100, blank = True)
    dateOfBirth = models.DateField(default = date.today)
    objects = models.Manager()
    def __str_(self):
        return self.user.username

class userregisteration(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)