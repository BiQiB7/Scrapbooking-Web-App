from django.shortcuts import render
from django.views import View
from scrapbook.models import Scrapbook
from discover.models import Topic
from .forms import CreateScrapbookForm
from django.db.models import Q

# Create your views here.
def discover(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    scrapbooks = Scrapbook.objects.filter(
    Q(topic__name__icontains=q) | 
    Q(name__icontains=q)
    )
    topics = Topic.objects.all()
    return render(request, 'discover/discover.html', {'scrapbooks': scrapbooks, 'topics': topics})
   
                #top = Topic(form.topic)
                #top.save()
                #new_scrapbook.topic.add(top)
                #new_scrapbook.save()
				# new_post.save()

			#for f in files:
			#	img = Image(image=f)
			#	img.save()
			#	new_post.image.add(img)
			#new_post.save()
def scrapbook(request, pk):
    scrapbook = Scrapbook.objects.get(id=pk)     
    return render(request, 'scrapbook/scrapbook.html', {'scrapbook': scrapbook})