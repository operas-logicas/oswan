# Generated by Django 3.1.4 on 2020-12-09 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201209_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='model',
            field=models.CharField(default={'placeholder': 'Model'}, max_length=100),
        ),
    ]