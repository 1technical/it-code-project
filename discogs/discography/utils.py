from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

menu = [
    {'title': "Артисты", 'url_name': 'artist_list'},
    {'title': "Добавить Артиста", 'url_name': 'artist_create'},
    {'title': "Добавить Альбом", 'url_name': 'album_create'},
]


class MenuMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu = user_menu[:1]
        context['menu'] = user_menu
        return context

class PersonalAcessMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)