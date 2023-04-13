from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import profile
from django.template import loader
from .forms import ImageForm
from .models import Image
from scrapbook.models import Scrapbook, Topic
from django.views import View
# Create your views here.


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = ImageForm()
            img = Image.objects.all()
            # form = createScrapbookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        return render(request, "profiles/profiles.html", {"img": img, "form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ImageForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                obj = form.instance
            return render(request, "profiles/profiles.html", {"obj": obj})
