from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#def index(request):
#    context = {
#        'variable':"this jiis sent"
        
#    }
#    return render(request,'scrapbook/index.html',context)

#def about(request):
#    return HttpResponse('This is about page')

#def services(request):
#    return HttpResponse('This is services page')

#def contact(request):
#    return HttpResponse('this is contact page')

def Profile(request):
    # user_object = User.objects.get(username = pk)
    # user_profile = Profile.objects.get(user = user_object)
    
    # context = {
    #    'user_object': user_object,
    #    'user_profile': user_profile,
    # }
    return render(request,'profiles/profiles.html')
