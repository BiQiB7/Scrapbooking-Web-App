from django.db import models
from django.contrib.auth.models import User

# Define db fields
class Profile(models.Model):
    # relation of user to User table
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #attibutes
    profile_pic = models.ImageField(
        upload_to = 'users/profile_pics',
        blank = True,
        null = True
    )
    bio = models.TextField(blank = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username