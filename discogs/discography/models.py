from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist', on_delete=models.DO_NOTHING)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        help_text="Формат даты: <ГГГГ>", verbose_name="Год релиза")
    genre = models.ManyToManyField('Genre')

    class Meta:
        ordering = ["artist", "year"]

    def __str__(self):
        return f"{self.artist} - {self.title}"


class Genre(models.Model):
    GENRES_CHOICES = [
        ("JAZZ", "Jazz"),
        ("HIPHOP", "Hip hop"),
        ("ROCK", "Rock"),
        ("POP", "Popular music"),
        ("ELECTRO", "Electronic"),
    ]

    title = models.CharField(max_length=8, choices=GENRES_CHOICES, verbose_name='genre')

    def __str__(self):
        return self.title
