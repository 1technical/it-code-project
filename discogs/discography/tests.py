from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
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
        data = {'name': self.artist.name, 'profile': self.artist.profile}
        response = self.client.post(reverse('artist_update', args=[self.artist.slug]),
                                    data=data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)

    def test_not_authenticated_user_can_not_create_artist(self):
        url = reverse('artist_create')
        data = {
            'name': 'New Artist Name',
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')


class AlbumTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = factories.ArtistFactory()
        self.album = factories.AlbumFactory(artist=self.artist)
        self.user = User.objects.create_user(
            username='user1', password='password1'
        )

    def test_album_create(self):
        response = self.client.post(path=reverse("album_create"), args={'slug': self.album.slug}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_get_absolute_url(self):
        self.artist = Artist.objects.create(name="Artist Name")
        album = Album.objects.create(title='Album Title', year='1999', artist=self.artist)
        self.assertEquals(album.get_absolute_url(), '/album/artist-name-album-title/')

    def test_album_delete(self):
        response = self.client.post(path=reverse("album_delete", args=[self.album.slug]), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_not_authenticated_user_can_not_create_album(self):
        url = reverse('album_create')
        data = {
            'title': 'New Album Name',
            'year': 1999,
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')
