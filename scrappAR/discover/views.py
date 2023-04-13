from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from scrapbook.models import Scrapbook, Topic
from .forms import createScrapbookForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from scrapbook.forms import CoverImageForm

# Create your views here.


class discoverView(View):
    def discover(request):
        form = createScrapbookForm(request.POST, request.FILES)
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        scrapbooks = Scrapbook.objects.filter(
            Q(topic__name__icontains=q) |
            Q(title__icontains=q)
        )
        topics = Topic.objects.all()
        return render(request, 'discover/discover.html', {'scrapbooks': scrapbooks, 'topics': topics, 'form': form, })

    def scrapbook(request, pk):
        scrapbook = Scrapbook.objects.get(id=pk)
        return render(request, 'scrapbook/scrapbook.html', {'scrapbook': scrapbook})


    def create_scrapbook(request):
        form = createScrapbookForm(request.POST or None)
        # if request.method == 'POST':
            # form = createScrapbookForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            topic_name = form.cleaned_data['topic']
            new_topic_name = form.cleaned_data['new_topic']

            if topic_name:
               topic = Topic.objects.filter(name=topic_name).first()
            else:
                topic = Topic.objects.filter(name=new_topic_name).first()
                if not topic:
                    topic = Topic.objects.create(name=new_topic_name)

            scrapbook = Scrapbook.objects.create(title=title, topic=topic)
            return redirect('scrapbook:scrapbook-detail', pk=scrapbook.pk)
            # else:
                # form = createScrapbookForm()

        context = {'form': form}
        return redirect('scrapbook:scrapbook-detail', pk=scrapbook.pk)
    # render(request, 'scrapbook:scrapbook-detail', context)