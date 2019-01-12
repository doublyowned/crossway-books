# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=50)
	medium = models.CharField(max_length=50)
	page_count = models.IntegerField()
	ISBN_10 = models.CharField(max_length=13)
	pic_url = models.CharField(max_length=200)