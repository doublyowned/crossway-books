# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=50, blank=True, default='')
	medium = models.CharField(max_length=50, blank=True, default='')
	page_count = models.IntegerField(null=True)
	ISBN_10 = models.CharField(max_length=13, blank=True, default='')
	pic_url = models.CharField(max_length=200, blank=True, default='')
	author = models.CharField(max_length=100)

	def __str__(self):
		return self.title + ' by ' + self.author