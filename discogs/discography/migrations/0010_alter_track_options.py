# Generated by Django 4.2.1 on 2023-05-08 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0009_alter_genre_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['album']},
        ),
    ]
