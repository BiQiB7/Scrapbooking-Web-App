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
def profile_view(request):
    profiles = profile.objects.all()
    # name = profile.objects.values_list('name', flat=True)
    # name = profile.objects.name
    # desc = profile.objects.values_list('desc', flat=True)

    # followers = profile.objects.values_list('followers', flat=True)
    # followers = profile.followers
     
    # template = loader.get_template('profiles/profiles.html')
    # context = {
    # 'name' : name,
    #  'desc' : desc,
    # 'followers' : followers,
  #} 
    context = {
      'profile' : profiles,
    }
    return render(request, 'profiles/profiles.html', context)
    # return HttpResponse(template.render(context, request))
