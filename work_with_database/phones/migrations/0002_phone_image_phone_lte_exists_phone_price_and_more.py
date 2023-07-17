# Generated by Django 4.2.3 on 2023-07-17 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(default='default url', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=datetime.date.today, verbose_name='release_date'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]