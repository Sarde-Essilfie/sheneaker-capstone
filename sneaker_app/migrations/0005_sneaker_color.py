# Generated by Django 4.1.4 on 2022-12-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0004_alter_sneaker_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='color',
            field=models.CharField(default='Not Available', max_length=200),
        ),
    ]
