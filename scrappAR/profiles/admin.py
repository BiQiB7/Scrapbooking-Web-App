from django.contrib import admin
# from users.models import Profile
# from .models import profile

# admin.site.register(profile)

# Register your models here.
from .models import Image

admin.site.register(Image)