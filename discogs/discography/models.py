from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('album_list', args=[self.slug])

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
    # manytomany
    title = models.CharField(max_length=255, choices=GENRES_CHOICES, verbose_name='genre')

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, max_length=255, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        help_text="Формат даты: <ГГГГ>", verbose_name="Год релиза")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["artist", "year"]

    def get_absolute_url(self):
        return reverse('album_detail', args=[self.slug])


class Track(models.Model):
    # onetomany
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name='albums')
    track_number = models.SmallIntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=255, null=True)
    ordering = ('album', 'track_number',)

    def __str__(self):
        return f'{self.track_number} - {self.title}'

    class Meta:
        ordering = ["track_number"]


