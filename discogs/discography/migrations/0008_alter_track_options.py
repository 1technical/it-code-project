# Generated by Django 4.2.1 on 2023-05-08 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0007_alter_track_options_alter_artist_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['track_number']},
        ),
    ]
