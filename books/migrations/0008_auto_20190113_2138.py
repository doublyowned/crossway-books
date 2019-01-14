# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-14 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190113_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[(None, 'Other'), ('Academic', 'Academic'), ('Apologetics', 'Apologetics'), ('Arts & Literature', 'Arts & Literature'), ('Bible Studies & Devotionals', 'Bible Studies & Devotionals'), ('Biblical Studies', 'Biblical Studies'), ('Children & Youth', 'Children & Youth'), ('Christian Living', 'Christian Living'), ('Church Ministry', 'Church Ministry'), ('Commentaries & Reference', 'Commentaries & Reference'), ('Culture & Social Issues', 'Culture & Social Issues'), ('Education', 'Education'), ('Evangelism & Missions', 'Evangelism & Missions'), ('Fiction', 'Fiction'), ('History & Biography', 'History & Biography'), ('Marriage & Family', 'Marriage & Family'), ('Theology', 'Theology'), ('Women', 'Women')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]