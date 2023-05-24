from discography.models import *

menu = [
    {'title': "Артисты", 'url_name': 'artist_list'},
    {'title': "Добавить Артиста", 'url_name': 'artist_create'},
    {'title': "Добавить Альбом", 'url_name': 'album_create'},
]


class MenuMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
