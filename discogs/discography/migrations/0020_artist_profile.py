# Generated by Django 4.2.1 on 2023-05-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0019_alter_track_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile',
            field=models.TextField(null=True),
        ),
    ]
