# Generated by Django 3.1.4 on 2020-12-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201208_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='engineCapacity',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='horsePower',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
