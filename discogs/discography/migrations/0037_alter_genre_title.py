# Generated by Django 4.2.1 on 2023-05-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0036_alter_genre_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(choices=[('', '----'), ('Jazz', 'Jazz'), ('Hip Hop', 'Hip hop'), ('Rock', 'Rock'), ('Pop', 'Popular music'), ('Electronic', 'Electronic'), ('Experimental', 'Experimental')], default='Pop', max_length=255, verbose_name='Жанр'),
        ),
    ]
