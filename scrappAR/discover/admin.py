from django.contrib import admin
# from scrapbook.models import Scrapbook
from .models import Topic, Scrapbook

admin.site.register(Scrapbook)
admin.site.register(Topic)
# Register your models here.