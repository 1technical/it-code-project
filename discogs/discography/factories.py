from datetime import datetime
import factory
from faker import Factory
from discography import models


factory_en = Factory.create('en-Us')


class ArtistFactory(factory.django.DjangoModelFactory):
    name = factory_en.word()
    profile = factory_en.text()

    class Meta:
        model = models.Artist


class AlbumFactory(factory.django.DjangoModelFactory):
    title = factory_en.word()
    artist = factory.SubFactory(ArtistFactory)
    year = factory_en.date_between_dates(date_start=datetime(1900, 1, 1), date_end=datetime(2023, 1, 1)).year

    class Meta:
        model = models.Album
