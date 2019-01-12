# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-12 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN_10',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='medium',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pic_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
