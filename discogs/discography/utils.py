from discography.models import *

menu = [{'title': "Music Library", 'url_name': 'index'},
        {'title': "Artist", 'url_name': 'artist'},
        {'title': "Album", 'url_name': 'album'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # user_menu = menu.copy()
        context['menu'] = menu
        return context
