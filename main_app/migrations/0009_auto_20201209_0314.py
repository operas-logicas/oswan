# Generated by Django 3.1.4 on 2020-12-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201209_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='description',
            field=models.TextField(),
        ),
    ]
