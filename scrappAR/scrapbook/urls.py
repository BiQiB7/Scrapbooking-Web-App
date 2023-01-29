from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView

urlpatterns = [
	path('scrapbook/', PostListView.as_view(), name='post-list'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('', PostListView.show_scrapbooks),
	path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
	path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
	path('post/<int:post_pk>/comment/delete/<int:pk>/',CommentDeleteView.as_view(), name='comment-delete'),
	path('scrapbook/<str:pk>', PostListView.scrapbook, name = 'scrapbook')
]