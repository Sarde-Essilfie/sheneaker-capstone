# Generated by Django 4.1.4 on 2022-12-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0015_alter_sneaker_gender_alter_sneaker_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='links',
            field=models.JSONField(blank=True, null=True),
        ),
    ]