from django.shortcuts import render
from django.views import View
from scrapbook.models import Scrapbook, Topic
from .forms import CreateScrapbookForm

# Create your views here.
class DiscoverView(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            scrapbooks = Scrapbook.objects.all()
            form = CreateScrapbookForm()
            context = {
                'scrapbooks': scrapbooks,
                'form':form,
            }
        return render(request, 'discover/discover.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            scrapbooks = Scrapbook.objects.all()
            form = CreateScrapbookForm(request.POST, request.FILES)
            # form.topic = 
			# files = request.FILES.getlist('image')
            if form.is_valid():
                new_scrapbook = form.save(commit=False)
            context = {
                'scrapbooks': scrapbooks,
                'form':form,
            }
        return render(request,'discover/discover.html', context)
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