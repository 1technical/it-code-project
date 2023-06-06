from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegistrationUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email уже сущетвует.')
        return data


class PasswordsChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)

    def clean_new_password2(self):
        data = self.cleaned_data
        if data['new_password1'] != data['new_password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['new_password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')


class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)

    def clean_name(self):
        name = self.cleaned_data['name']
        if Artist.objects.filter(name=name.title()).exists():
            raise ValidationError(f"Артист с именем {name.title()} уже существует")
        return name


class UpdateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'profile', 'photo',)


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'genre', 'photo',)


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
            raise ValidationError(f"Трек с именем {title.title()} уже существует")
        return title


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'content', 'rating',)
