# Generated by Django 4.2.1 on 2023-05-08 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0010_alter_track_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['album', 'track_number']},
        ),
    ]
