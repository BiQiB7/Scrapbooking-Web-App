from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView

urlpatterns = [
	path('', PostListView, name='post-list'),
	path(' post/<int:pk>/', PostDetailView, name='post-detail'),
	path(' post/edit/<int:pk>/', PostEditView, name='post-edit'),
	path(' post/delete/<int:pk>/', PostDeleteView, name='post-delete'),
	path(' post/<int:post_pk>/comment/delete/<int:pk>/', name='comment-delete'),
]