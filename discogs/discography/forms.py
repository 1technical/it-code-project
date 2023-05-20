from django import forms
from django.core.exceptions import ValidationError

from .models import *


class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)

    widgets = {
        'profile': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
    }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Artist.objects.filter(name=name).exists():
            raise ValidationError(f"Артист с именем {name} существует")
        return name


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'genre', 'photo',)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Album.objects.filter(title=title).exists():
            raise ValidationError(f"Альбом с названием {title} уже существует")
        return title


class TracklistForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('artist', 'album', 'track_number', 'title', 'duration',)

    def clean_track_number(self):
        track_number = self.cleaned_data['track_number']
        if Track.objects.filter(track_number=track_number).exists():
            raise ValidationError(f"Трек под номером {track_number} уже существует")
        return track_number
