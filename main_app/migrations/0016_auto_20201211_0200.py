# Generated by Django 3.1.4 on 2020-12-11 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20201211_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='favorites',
            new_name='likes',
        ),
    ]
