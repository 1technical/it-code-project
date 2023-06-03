from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.urls import reverse
from slugify import slugify


class Artist(models.Model):
    name = models.CharField("Имя", max_length=255, unique=True)
    profile = models.TextField("Профиль", blank=True)
    photo = models.ImageField("Фото", upload_to="artist", default='artist/singer.png')
    slug = models.SlugField("URL", max_length=255, unique=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('artist_profile', args=[self.slug])

    class Meta:
        ordering = ("name",)


class Genre(models.Model):
    GENRES_CHOICES = (
        ("Jazz", "Jazz"),
        ("Hip Hop", "Hip hop"),
        ("Rock", "Rock"),
        ("Pop", "Popular music"),
        ("Electronic", "Electronic"),
        ("Experimental", "Experimental"),
    )
    title = models.CharField(max_length=255, choices=GENRES_CHOICES, default='Pop', verbose_name='Жанр')

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField("Название", max_length=255)
    artist = models.ForeignKey(Artist, max_length=255, null=True, on_delete=models.CASCADE, related_name='albums',
                               verbose_name="Артист")
    photo = models.ImageField("Обложка", upload_to="album", default='album/vinyl.png')
    slug = models.SlugField("URL", max_length=255, unique=True)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        verbose_name="Год релиза")
    genre = models.ManyToManyField(Genre, related_name='albums', verbose_name="Жанр")

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.artist}-{self.title}')
        super(Album, self).save(*args, **kwargs)

    class Meta:
        ordering = ("artist", "year",)

    def get_absolute_url(self):
        return reverse('album_detail', args=[self.slug])


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name='tracks', verbose_name="Альбом")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, related_name='tracks',
                               verbose_name="Артист")
    track_number = models.PositiveSmallIntegerField("Номер", null=True)
    title = models.CharField("Название", max_length=100, null=True)
    duration = models.CharField("Длина", max_length=255, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ("track_number",)


class Review(models.Model):
    RATING_RANGE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    album = models.ForeignKey(Album,
                              on_delete=models.CASCADE,
                              related_name='reviews')
    name = models.CharField("Имя", max_length=255)
    email = models.EmailField("Email")
    content = models.TextField("Обзор")
    rating = models.IntegerField("Оценка", choices=RATING_RANGE, default=1)
    created = models.DateTimeField("Создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлен", auto_now=True)
    active = models.BooleanField("Статус", default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Обзор от {self.name} к {self.album}'
