from django import forms
from .models import *


class ArtistSearch(forms.Form):
    name = forms.CharField(label='Поиск по артисту', required=False)


class CreateArtistForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)

    widgets = {
        'profile': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
    }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'genre', 'photo',)

    tracks = forms.ModelMultipleChoiceField(
        queryset=Track.objects.all()
    )
