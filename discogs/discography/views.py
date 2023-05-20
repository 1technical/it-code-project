from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from discography.forms import CreateArtistForm, CreateAlbumForm, TracklistForm
from discography.models import *


class IndexView(ListView):
    model = Artist
    template_name = 'discography/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class SearchResultView(ListView):
    model = Artist
    template_name = 'discography/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Artist.objects.filter(name__icontains=query)


class ArtistListView(ListView):
    model = Artist
    template_name = 'discography/artist_list.html'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список артистов'
        return context


class ArtistProfileView(ListView):
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


class ArtistCreateView(CreateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = 'discography/artist_create.html'
    success_url = reverse_lazy('artist_list')
    raise_exception = True



class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = 'discography/artist_update.html'
    success_url = reverse_lazy('artist_list')


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


class AlbumCreateView(CreateView):
    form_class = CreateAlbumForm
    template_name = 'discography/album_create.html'
    success_url = reverse_lazy('artist_list')


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'discography/album_update.html'
    success_url = reverse_lazy('artist_list')


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'discography/album_delete.html'
    success_url = reverse_lazy('artist_list')


class TracklistCreateView(CreateView):
    form_class = TracklistForm
    template_name = 'discography/tracklist_create.html'
    success_url = reverse_lazy('artist_list')
