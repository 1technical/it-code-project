from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.urls import reverse
from slugify import slugify

class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    profile = models.TextField(null=True, blank=True, verbose_name="Профиль")
    photo = models.ImageField(upload_to="artist", default='artist/singer.png', verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

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
        ("Electronic", "Electronic"),
    ]
    title = models.CharField(max_length=255, choices=GENRES_CHOICES, verbose_name='Жанр')

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    artist = models.ForeignKey(Artist, max_length=255, null=True, on_delete=models.CASCADE, related_name='albums', verbose_name="Артист")
    photo = models.ImageField(upload_to="album", default='album/vinyl.png', verbose_name="Обложка")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        verbose_name="Год релиза")
    genre = models.ManyToManyField(Genre, related_name='albums', verbose_name='Жанр')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)

    class Meta:
        ordering = ["artist", "year"]

    def get_absolute_url(self):
        return reverse('album_detail', args=[self.slug])


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name='tracks', verbose_name="Альбом")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, related_name='tracks', verbose_name="Артист")
    track_number = models.PositiveSmallIntegerField(null=True, verbose_name="Номер")
    title = models.CharField(max_length=100, null=True, verbose_name="Название")
    duration = models.CharField(max_length=255, null=True, verbose_name="Длина")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ["track_number"]
