# Generated by Django 4.2.1 on 2023-06-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0046_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0),
        ),
    ]
