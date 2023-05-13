from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from discography.models import *


class IndexView(ListView):
    model = Artist
    template_name = 'discography/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'discography/artist_list.html'


class ArtistProfileListView(ListView):
    model = Artist
    template_name = 'discography/artist_profile.html'

    def get_queryset(self):
        self.slug = get_object_or_404(Artist, slug=self.kwargs["slug"])
        return Artist.objects.filter(slug=self.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль артиста'
        context['artist'] = Artist.objects.filter(name=self.slug)
        context['album_list'] = Album.objects.filter(artist__name=self.slug)
        return context


class AlbumDetailView(ListView):
    model = Album
    template_name = 'discography/album_detail.html'

    def get_queryset(self):
        self.slug = get_object_or_404(Album, slug=self.kwargs["slug"])
        return Album.objects.filter(slug=self.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Треклист'
        context['album'] = Album.objects.filter(title=self.slug)
        context['tracklist'] = Track.objects.filter(album__title=self.slug)
        return context
