from django.urls import path
from discography.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artist/<slug:slug>/', ArtistProfileListView.as_view(), name='artist_profile'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('artist_create/', ArtistCreateView.as_view(), name='artist_create'),
    path('album_create/', AlbumCreateView.as_view(), name='album_create'),
    path('artist_update/<slug:slug>', ArtistUpdateView.as_view(), name='artist_update'),
    path('album_update/<slug:slug>', AlbumUpdateView.as_view(), name='album_update'),
    path('album_delete/<slug:slug>', AlbumDeleteView.as_view(), name='album_delete'),
    path('search_result/', SearchResultView.as_view(), name='search_result'),
    path('tracklist_create/', TracklistCreateView.as_view(), name='tracklist_create'),

]
