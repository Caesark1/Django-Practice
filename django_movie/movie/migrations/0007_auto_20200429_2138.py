# Generated by Django 3.0.5 on 2020-04-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20200413_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='moviestar',
            name='value',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
    ]
