# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils.encoding import python_2_unicode_compatible

import django_filters

@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    pic_url = models.CharField(max_length=200)
    blurb = models.TextField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Book(models.Model):
    CATEGORY_CHOICES = (
        (None, 'Other'),
        ('Evangelism & Missions', 'Evangelism & Missions'),
        ('Commentaries & Reference', 'Commentaries & Reference'),
        ('Church Ministry', 'Church Ministry'),
        ('Arts & Literature', 'Arts & Literature'),
        ('Academic', 'Academic'),
        ('Theology', 'Theology'),
        ('Christian Living', 'Christian Living'),
        ('Apologetics', 'Apologetics'),
        ('Bible Studies & Devotionals', 'Bible Studies & Devotionals'),
        ('Biblical Studies', 'Biblical Studies'),
        ('Education', 'Education')
    )

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=None)
    medium = models.CharField(max_length=50, blank=True, default='')
    page_count = models.IntegerField(null=True)
    ISBN_10 = models.CharField(max_length=13, blank=True, default='')
    pic_url = models.CharField(max_length=200, blank=True, default='')
    blurb = models.TextField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def __unicode__(self):
        return '%s' % (self.title)

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['category', 'medium', 'author']
