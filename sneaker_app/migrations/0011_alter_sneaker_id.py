# Generated by Django 4.1.4 on 2022-12-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0010_alter_sneaker_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
