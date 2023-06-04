from django.urls import path

from discography.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('password_change/', PasswordsChangingView.as_view(), name='password_change'),
    path('password_change/done', password_change_done, name='password_change_done'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artist_create/', ArtistCreateView.as_view(), name='artist_create'),
    path('artist/<slug:slug>/', ArtistProfileView.as_view(), name='artist_profile'),
    path('artist_update/<slug:slug>', ArtistUpdateView.as_view(), name='artist_update'),
    path('search_result/', SearchResultView.as_view(), name='search_result'),
    path('album_create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album_update/<slug:slug>', AlbumUpdateView.as_view(), name='album_update'),
    path('album_delete/<slug:slug>', AlbumDeleteView.as_view(), name='album_delete'),
    path('tracklist_create/', TracklistCreateView.as_view(), name='tracklist_create'),
    path('<slug:slug>/review', album_review, name='album_review'),
]
