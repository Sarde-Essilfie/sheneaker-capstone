# Generated by Django 4.1.4 on 2022-12-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0007_alter_sneaker_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='links',
            field=models.URLField(default='https://stockx.com/nike-dunk-low-mineral-teal-gs'),
        ),
    ]
