from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from discography.forms import CreateArtistForm, CreateAlbumForm, TracklistForm, UpdateAlbumForm, UpdateArtistForm, \
    LoginUserForm, RegistrationUserForm, ReviewForm, PasswordsChangingForm
from discography.models import *
from discography.utils import MenuMixin, PersonalAcessMixin


class IndexView(MenuMixin, ListView):
    model = Artist
    template_name = 'discography/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class RegistrationUser(MenuMixin, CreateView):
    form_class = RegistrationUserForm
    template_name = 'discography/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


def password_change_done(request):
    return render(request, 'discography/password_change_done.html')


class PasswordsChangingView(MenuMixin, PersonalAcessMixin, PasswordChangeView):
    form_class = PasswordsChangingForm
    template_name = 'discography/password_change.html'
    success_url = reverse_lazy('password_change_done')


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


class ArtistCreateView(PersonalAcessMixin, MenuMixin, CreateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = 'discography/artist_create.html'
    success_url = reverse_lazy('artist_list')


class ArtistUpdateView(PersonalAcessMixin, MenuMixin, UpdateView):
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
        context['reviews'] = Review.objects.filter(album=self.slug, active=True)
        context['form'] = ReviewForm()
        return context


class AlbumCreateView(PersonalAcessMixin, MenuMixin, CreateView):
    form_class = CreateAlbumForm
    template_name = 'discography/album_create.html'
    success_url = reverse_lazy('artist_list')


class AlbumUpdateView(PersonalAcessMixin, MenuMixin, UpdateView):
    model = Album
    form_class = UpdateAlbumForm
    template_name = 'discography/album_update.html'
    success_url = reverse_lazy('artist_list')


class AlbumDeleteView(PersonalAcessMixin, MenuMixin, DeleteView):
    model = Album
    template_name = 'discography/album_delete.html'
    success_url = reverse_lazy('artist_list')


class TracklistCreateView(PersonalAcessMixin, MenuMixin, CreateView):
    form_class = TracklistForm
    template_name = 'discography/tracklist_create.html'
    success_url = reverse_lazy('artist_list')


@require_POST
def album_review(request, slug):
    menu = [
        {'title': "Артисты", 'url_name': 'artist_list'},
        {'title': "Добавить Артиста", 'url_name': 'artist_create'},
        {'title': "Добавить Альбом", 'url_name': 'album_create'},
    ]
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu = user_menu[:1]
    album = get_object_or_404(Album, slug=slug)
    review = None
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.album = album
        review.save()
    album = Album.objects.filter(slug=slug)
    return render(request, 'discography/album_review.html',
                  {'album': album,
                   'form': form,
                   'reviews': review,
                   'menu': user_menu})
