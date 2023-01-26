from django.contrib import admin
from .models import Posts,Comment,Likes, Image
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Image)