# Generated by Django 4.1.4 on 2022-12-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0013_alter_sneaker_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sneaker',
            old_name='link',
            new_name='links',
        ),
        migrations.AddField(
            model_name='sneaker',
            name='gender',
            field=models.CharField(default='women', max_length=200),
        ),
    ]
