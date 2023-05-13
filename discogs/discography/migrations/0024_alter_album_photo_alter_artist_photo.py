# Generated by Django 4.2.1 on 2023-05-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0023_alter_album_photo_alter_artist_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ImageField(default='album/vinyl.png', upload_to='album', verbose_name='Обложка Альбома'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.ImageField(default='artist/singer.png', upload_to='artist', verbose_name='Фото Артиста'),
        ),
    ]
