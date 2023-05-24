from django.test import TestCase, Client
from django.urls import reverse
from discography import models
from discography import factories
from discography.models import Artist, Album


class ArtistTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = factories.ArtistFactory()

    def test_artist_list(self):
        response = self.client.get(reverse('artist_list'))
        self.assertEquals(response.status_code, 200)

    def test_get_absolute_url(self):
        artist = Artist.objects.create(name='Artist Name')
        self.assertEquals(artist.get_absolute_url(), '/artist/artist-name/')

    def test_artist_detail(self):
        response = self.client.get(reverse('artist_profile', kwargs={'slug': self.artist.slug}))
        self.assertEquals(response.status_code, 200)

    def test_artist_create(self):
        data = {'name': 'John Johnoson', 'profile': 'Famous musician'}
        response = self.client.post(path=reverse('artist_create'), data=data, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_artist_update(self):
        data = {'name': self.artist.name + 'char', 'profile': self.artist.profile + 'some text'}
        response = self.client.post(reverse('artist_update', args=[self.artist.slug]),
                                    data=data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        upd_artist = models.Artist.objects.first()
        self.assertListEqual([self.artist.name + 'char', self.artist.profile + 'some text'],
                             [upd_artist.name, upd_artist.profile])
        self.assertEqual(response.status_code, 200)


class AlbumTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = factories.ArtistFactory()
        self.album = factories.AlbumFactory(artist=self.artist)

    def test_album_create(self):
        response = self.client.post(path=reverse("album_create"), args={'slug': self.album.slug}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_get_absolute_url(self):
        album = Album.objects.create(title='Album Title', year='1999')
        self.assertEquals(album.get_absolute_url(), '/album/album-title/')

    def test_album_delete(self):
        response = self.client.post(path=reverse("album_delete", args=[self.album.slug]), follow=True)
        self.assertEqual(response.status_code, 200)


class CreateAlbumFormTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_unique_name(self):
        Album.objects.create(title='Название', year='1999')
        album_count = Album.objects.count()
        data = {'title': 'Название', 'year': '2000'}
        response = self.client.post(path=reverse('album_create'), data=data, follow=True)
        self.assertEqual(Album.objects.count(), album_count)

        self.assertFormError(response, 'form', 'title', 'Альбом с названием Название уже существует')
        self.assertEqual(response.status_code, 200)
