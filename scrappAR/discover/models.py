from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Scrapbook(models.Model):
    
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    
