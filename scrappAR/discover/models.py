from django.db import models
from scrapbook.models import Scrapbook

# Create your models here.


class Discover(models.Model):
    scrapbooks = Scrapbook.objects.all()
    
