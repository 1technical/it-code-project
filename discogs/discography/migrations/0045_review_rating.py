# Generated by Django 4.2.1 on 2023-06-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0044_review_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
    ]
