from django.urls import path
from discography.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artist/<slug:slug>/', ArtistProfileListView.as_view(), name='artist_profile'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),

]
