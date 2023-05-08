from django.urls import path
from discography.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artist/<slug:slug>/', AlbumListView.as_view(), name='album_list'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),

]
