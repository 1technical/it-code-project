from django import forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import *


class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)

    widgets = {
        'profile': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
    }


class UpdateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)



class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'genre', 'photo',)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Album.objects.filter(title=title).exists():
            raise ValidationError(f"Альбом с названием {title} уже существует")
        return title


class UpdateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'genre', 'photo',)


class TracklistForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('artist', 'album', 'track_number', 'title', 'duration',)

    def clean_title(self):
        title = self.cleaned_data['title']
        number = self.cleaned_data['track_number']
        if Track.objects.filter(title=title, track_number=number).exists():
            raise ValidationError(f"Трек с именем {title} уже существует")
        return title
