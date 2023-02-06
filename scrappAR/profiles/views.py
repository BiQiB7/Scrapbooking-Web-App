from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from users.models import Profile
from django.views import View

from django.shortcuts import render
from django.http import HttpResponse
from .models import profile
from django.template import loader
# Create your views here.
def home(request):
    proz = profile.objects.values_list('name', flat=True)
    prof = profile.objects.values_list('desc', flat=True)
    prod = profile.objects.values_list('followers', flat=True)
    
     
    template = loader.get_template('profiles/profiles.html')
    context = {
    'mem': proz,
    'can': prof,
    'dam': prod
    
  }
    
    return HttpResponse(template.render(context, request))
