from django.shortcuts import render
from django.http import HttpResponse
# from .models import profile
from django.template import loader
from .forms import ImageForm
from .models import Image

# Create your views here.
def index(request):
    if request.method == "POST":
     form=ImageForm(data=request.POST,files=request.FILES)
     if form.is_valid():
       form.save()
       obj=form.instance
       return render(request,"profiles/profiles.html",{"obj":obj})
    else:
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"profiles/profiles.html",{"img":img,"form":form})