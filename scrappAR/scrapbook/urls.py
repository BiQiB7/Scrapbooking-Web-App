from django.urls import path
from .views import PostListView, PostDeleteView, DeleteScrapbookView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('scrapbook/', PostListView.as_view(), name='post-list'),
    path('scrapbook/<int:pk>/', PostListView.as_view(), name='scrapbook-detail'),
    path('scrapbook/delete/<int:pk>',DeleteScrapbookView.as_view(), name='scrapbook-delete'),
    # path('scrapbook/<int:pk>/upload_cover/',PostListView.upload_cover, name='upload-cover'),
    path('merging/', PostListView.take_picture, name='merging'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    # path('delete/<post_id>',PostListView.delete_post,name='delete'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('', PostListView.show_scrapbooks),
    # path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),

    # path('post/<int:post_pk>/comment/delete/<int:pk>/',CommentDeleteView.as_view(), name='comment-delete'),
    # path('scrapbook/<str:pk>/', PostListView.scrapbook, name = 'scrapbook'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
