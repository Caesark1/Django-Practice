# Generated by Django 3.0.5 on 2020-04-06 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='world_premieres',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
