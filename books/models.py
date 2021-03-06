# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils.encoding import python_2_unicode_compatible

import django_filters

@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pic_url = models.CharField(max_length=200)
    blurb = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % (self.name)

@python_2_unicode_compatible
class Book(models.Model):
    CATEGORY_CHOICES = (
        (None, 'Other'),
        ('Academic', 'Academic'),
        ('Apologetics', 'Apologetics'),
        ('Arts & Literature', 'Arts & Literature'),
        ('Bible Studies & Devotionals', 'Bible Studies & Devotionals'),
        ('Biblical Studies', 'Biblical Studies'),
        ('Children & Youth', 'Children & Youth'),
        ('Christian Living', 'Christian Living'),
        ('Church Ministry', 'Church Ministry'),
        ('Commentaries & Reference', 'Commentaries & Reference'),
        ('Culture & Social Issues', 'Culture & Social Issues'),
        ('Education', 'Education'),
        ('Evangelism & Missions', 'Evangelism & Missions'),
        ('Fiction', 'Fiction'),
        ('History & Biography', 'History & Biography'),
        ('Marriage & Family', 'Marriage & Family'),
        ('Theology', 'Theology'),
        ('Women', 'Women'),
    )

    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=None)
    medium = models.CharField(max_length=50, blank=True, default='')
    page_count = models.IntegerField(null=True)
    ISBN_10 = models.CharField(max_length=13, blank=True, default='')
    pic_url = models.CharField(max_length=200, blank=True, default='')
    blurb = models.TextField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        text = self.title
        if self.author:
            text += ' by ' + self.author.name
        return text

    def __unicode__(self):
        return u'%s' % (self.title)

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['category', 'author']
