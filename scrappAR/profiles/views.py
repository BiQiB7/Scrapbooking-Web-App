from django.shortcuts import render

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
    return render(request,'profiles/profiles.html')
