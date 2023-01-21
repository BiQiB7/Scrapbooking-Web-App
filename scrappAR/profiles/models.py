from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
# Create your models here.
User = get_user_model()
class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank = True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(default = 1)
    bio = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'blank-user.jpg' )
    location = models.CharField(max_length = 100, blank = True)
    
    def __str_(self):
        return self.id_user
# Create your models here.
