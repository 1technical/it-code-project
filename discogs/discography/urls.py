from django.urls import path
from discography.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artist/<slug:slug>/', ArtistProfileListView.as_view(), name='artist_profile'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('artist_create/', ArtistCreate.as_view(), name='artist_create'),
    path('album_create/', AlbumCreate.as_view(), name='album_create'),
    path('artist_update/<slug:slug>', ArtistUpdate.as_view(), name='artist_update'),
    path('album_update/<slug:slug>', AlbumUpdate.as_view(), name='album_update'),

]
