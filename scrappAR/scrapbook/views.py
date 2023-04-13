from .models import Image
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Posts, Comment, Likes, Scrapbook, Image
from .forms import PostForm, CoverImageForm
from django.views.generic import UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Scrapbook
from django.core.files.storage import FileSystemStorage



class PostListView(View):
    template_name = 'scrapbook/post_list.html'

    def get(self, request, *args, **kwargs):
        scrapbook = get_object_or_404(Scrapbook, pk=kwargs['pk'])
        post = Posts.objects.filter(
            scrapbook=scrapbook).order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': post,
            'form': form,
            'scrapbook': scrapbook,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        scrapbook = get_object_or_404(Scrapbook, pk=kwargs['pk'])
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.scrapbook = scrapbook
            new_post.save()

            for f in request.FILES.getlist('image'):
                img = Image(image=f)
                img.save()
                new_post.image.add(img)

            form = PostForm()

        post = Posts.objects.filter(
            scrapbook=scrapbook).order_by('-created_on')
        context = {
            'post_list': post,
            'form': form,
            'scrapbook': scrapbook,
        }

        return render(request, self.template_name, context)

    def take_picture(request):
        return render(request, 'scrapbook/merging.html')
    

    
class DeleteScrapbookView(DeleteView):
    model = Scrapbook
    success_url = reverse_lazy('discover:discover')

    def post(self, request, *args, **kwargs):
        # scrapbook_pk = request.POST.get('pk')
        scrapbook = Scrapbook.objects.get(pk=kwargs['pk'])
        messages.success(request, 'Scrapbook "{}" deleted successfully!'.format(scrapbook.title))
        return super().post(request, *args, **kwargs)
    
from django.urls import reverse_lazy

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'scrapbook/post_delete.html'

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook-detail', kwargs={'pk': self.object.scrapbook.pk})

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise Http404
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)

    


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'scrapbook/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
