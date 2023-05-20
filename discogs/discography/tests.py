from django.test import TestCase, Client
from django.urls import reverse
from discography import models
from discography import factories


class ArtistTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = factories.ArtistFactory()

    def test_artist_list(self):
        response = self.client.get(reverse('artist_list'))
        self.assertEquals(response.status_code, 200)

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
        self.assertListEqual([self.artist.name, self.artist.profile],
                             [upd_artist.name, upd_artist.profile])


class AlbumTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = factories.ArtistFactory()
        self.album = factories.AlbumFactory(artist=self.artist)

    def test_album_create(self):
        response = self.client.post(path=reverse("album_create"), args={'slug': self.album.slug}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_album_delete(self):
        response = self.client.post(path=reverse("album_delete", args=[self.album.slug]), follow=True)
        self.assertEqual(response.status_code, 200)
