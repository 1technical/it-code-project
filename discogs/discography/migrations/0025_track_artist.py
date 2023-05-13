# Generated by Django 4.2.1 on 2023-05-12 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0024_alter_album_photo_alter_artist_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discography.artist'),
        ),
    ]