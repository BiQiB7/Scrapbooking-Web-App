from django.urls import path, include
from users import views as usersview
from main import views as mainview
from django.urls import re_path as url
from scrapbook import views as scrapbookviews
from profiles import views as profileviews
urlpatterns = [
    # path('users/register', usersview.user_registration.as_view(), name = 'register'),
    # path('scrapbook/listview', scrapbookviews.PostListView.as_view(), name = 'listview'),
    #path('scrapbook/detailview',scrapbookviews.PostDetailView.as_view(), name = 'detailview'),
    # path('scrapbook/edit',scrapbookviews.PostEditView.as_view(), name = 'edit' ),
    # path('scrapbook/delete',scrapbookviews.DeleteView.as_view(),name = 'delete'),
    # path('scrapbook/comment',scrapbookviews., name = 'comment'),
    # comment & delete view?
]