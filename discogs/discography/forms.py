from django import forms
from .models import *


class CreateArtistForm(forms.ModelForm):
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


class TracklistForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
