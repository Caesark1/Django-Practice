# Generated by Django 3.0.5 on 2020-04-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200410_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, max_length=155, unique=True),
        ),
    ]
