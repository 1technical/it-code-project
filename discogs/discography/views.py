from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from discography.forms import CreateArtistForm, CreateAlbumForm, TracklistForm, UpdateAlbumForm, UpdateArtistForm, \
    LoginUserForm, RegisterUserForm
from discography.models import *
from discography.utils import MenuMixin


class IndexView(MenuMixin, ListView):
    model = Artist
    template_name = 'discography/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class RegisterUser(MenuMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'discography/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(MenuMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'discography/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


class SearchResultView(MenuMixin, ListView):
    model = Artist
    template_name = 'discography/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class ArtistListView(MenuMixin, ListView):
    model = Artist
    template_name = 'discography/artist_list.html'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список артистов'
        return context


class ArtistProfileView(MenuMixin, ListView):
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


class ArtistCreateView(MenuMixin, CreateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = 'discography/artist_create.html'
    success_url = reverse_lazy('artist_list')
    raise_exception = True

class ArtistUpdateView(MenuMixin, UpdateView):
    model = Artist
    form_class = UpdateArtistForm
    template_name = 'discography/artist_update.html'
    success_url = reverse_lazy('artist_list')


class AlbumDetailView(MenuMixin, ListView):
    model = Album
    template_name = 'discography/album_detail.html'

    def get_queryset(self):
        self.slug = get_object_or_404(Album, slug=self.kwargs["slug"])
        return Album.objects.filter(slug=self.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Альбом'
        context['album'] = Album.objects.filter(title=self.slug)
        context['tracklist'] = Track.objects.filter(album__title=self.slug)
        return context

class AlbumCreateView(MenuMixin, CreateView):
    form_class = CreateAlbumForm
    template_name = 'discography/album_create.html'
    success_url = reverse_lazy('artist_list')


class AlbumUpdateView(MenuMixin, UpdateView):
    model = Album
    form_class = UpdateAlbumForm
    template_name = 'discography/album_update.html'
    success_url = reverse_lazy('artist_list')


class AlbumDeleteView(MenuMixin, DeleteView):
    model = Album
    template_name = 'discography/album_delete.html'
    success_url = reverse_lazy('artist_list')

class TracklistCreateView(MenuMixin, CreateView):
    form_class = TracklistForm
    template_name = 'discography/tracklist_create.html'
    success_url = reverse_lazy('artist_list')
