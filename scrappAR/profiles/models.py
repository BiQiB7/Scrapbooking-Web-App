from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    followers = models.IntegerField()
# Create your models here.
