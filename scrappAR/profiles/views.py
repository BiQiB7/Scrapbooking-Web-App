from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from users.models import Profile
from django.views import View

def profile(request, pk):
       # pk = self.kwargs.get('pk')
    user_object = User.objects.get(id = pk)
    user_profile = Profile.objects.get(user = user_object)
    
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        }
        
    return render(request,'profiles/profiles.html')
