# Generated by Django 4.2.1 on 2023-05-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0008_alter_track_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(choices=[('Jazz', 'Jazz'), ('Hip Hop', 'Hip hop'), ('Rock', 'Rock'), ('Pop', 'Popular music'), ('Eelectronic', 'Electronic')], max_length=255, verbose_name='жанр'),
        ),
    ]
