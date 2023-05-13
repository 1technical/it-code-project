from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from discography import forms
from discography.forms import CreateArtistForm, CreateAlbumForm, ArtistSearch
from discography.models import *


class IndexView(ListView):
    model = Artist
    template_name = 'discography/index.html'

    # def get_queryset(self):
    #     name = self.request.GET.get('name')
    #     qs = Artist.objects.all()
    #     if name:
    #         return qs.filter(name__icontains=name)
    #     return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        # context['form'] = forms.ArtistSearch()
        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'discography/artist_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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

class ArtistCreate(CreateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = 'discography/artist_create.html'
    success_url = reverse_lazy('artist_list')

class AlbumCreate(CreateView):
    form_class = CreateAlbumForm
    template_name = 'discography/album_create.html'
    success_url = reverse_lazy('artist_list')


