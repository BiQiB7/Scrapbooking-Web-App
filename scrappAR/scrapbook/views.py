from .models import Image
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Posts, Comment, Likes
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt


class PostListView(View):
	def get(self, request, *args, **kwargs):
		if request.method =="GET":
			post = Posts.objects.all().order_by('-created_on')
			form = PostForm()
			context = {
				'post_list': post,
				'form': form,
			} 

		return render(request, 'scrapbook/post_list.html', context)

	def post(self, request, *args, **kwargs):
		if request.method == "POST":
			post = Posts.objects.all().order_by('-created_on')
			form = PostForm(request.POST, request.FILES)
			files = request.FILES.getlist('image')

			if form.is_valid():
				new_post = form.save(commit=False)
				new_post.author = request.user
				new_post.save()

			for f in files:
				img = Image(image=f)
				img.save()
				new_post.image.add(img)
			new_post.save()
				

			context = {
				'post_list': post,
				'form': form,
			}

		return render(request, 'scrapbook/post_list.html', context)

class PostDetailView(View):
	def gets(self, request, pk, *args, **kwargs):
		post = Posts.objects.get(pk=pk)
		form = CommentForm()
		comments = Comment.objects.filter(post=post).order_by('-created_on')

		context = {
			'post' : post,
			'form' : form,
			'comments' : comments,
		}

		return render(request, 'scrapbook/post_details.html', context)

	def post(self, request, pk, *args, **kwargs):
		post = Post.objects.get(pk=pk)
		form = CommentForm(request.POST)

		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.author = request.user
			new_comment.post = post
			new_comment.save()

		comments = Comment.objects.filter(post=post).order_by('-created_on')

		context = {
			'post' : post,
			'form' : form,
			'comments': comments,
		}

		return render(request, 'scrapbook/post_details.html', context)

	def like(request, post_id):
		user = request.user
		post = Post.objects.get(id=post_id)
		current_likes = post.likes 
		liked = Likes.objects.filter(user=user, post=post).count()
		if not liked:
			liked = Likes.objects.create(user=user, post=post)
			current_likes = current_likes + 1
		else: 
			liked = Likes.objects.filter(user=user, post=post).delete()
			current_likes = current_likes - 1

		post.likes = current_likes
		post.saw()
		return HttpResponseRedirect(reverse('post-detail', args=[post_id]))

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Posts
	fields = ['body']
	template_name = 'scrapbook/post_edit.html'

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('post-detail', kwargs={'pk': pk})

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Posts
	template_name = 'scrapbook/post_delete.html'
	success_url = reverse_lazy('post-list')

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'scrapbook/comment_delete.html'

	def get_success_url(self):
		pk = self.kwargs['post_pk']
		return reverse_lazy('post-detail', kwargs={'pk': pk})

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author
