# Generated by Django 3.1.4 on 2020-12-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201209_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='engineCapacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='horsePower',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='year',
            field=models.IntegerField(),
        ),
    ]