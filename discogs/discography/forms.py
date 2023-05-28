from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)


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
