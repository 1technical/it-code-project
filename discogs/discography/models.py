from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name='Артист')
    profile = models.TextField(null=True, blank=True, verbose_name="Профиль артиста")
    photo = models.ImageField(upload_to="artist", default='artist/singer.png', verbose_name="Фото Артиста")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artist_profile', args=[self.slug])

    class Meta:
        ordering = ["name"]

class Genre(models.Model):
    GENRES_CHOICES = [
        ("Jazz", "Jazz"),
        ("Hip Hop", "Hip hop"),
        ("Rock", "Rock"),
        ("Pop", "Popular music"),
        ("Eelectronic", "Electronic"),
    ]
    title = models.CharField(max_length=255, choices=GENRES_CHOICES, verbose_name='Жанр')

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название альбома")
    artist = models.ForeignKey(Artist, max_length=255, on_delete=models.CASCADE, verbose_name="Артист")
    photo = models.ImageField(upload_to="album", default='album/vinyl.png', verbose_name="Обложка Альбома")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        help_text="Формат даты: <ГГГГ>", verbose_name="Год релиза")
    genre = models.ManyToManyField(Genre, related_name='albums')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["artist", "year"]

    def get_absolute_url(self):
        return reverse('album_detail', args=[self.slug])


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name='albums', verbose_name="Альбом")
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE, verbose_name="Артист")
    track_number = models.PositiveSmallIntegerField(null=True, verbose_name="Номер")
    title = models.CharField(max_length=100, null=True, verbose_name="Название")
    duration = models.CharField(max_length=255, null=True, verbose_name="Продолжительность")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ["track_number"]


