# Generated by Django 3.1.4 on 2020-12-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201209_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]