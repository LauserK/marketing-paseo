# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Image(models.Model):
	file    = models.FileField(upload_to="images/", blank=True, default="")
	time    = models.IntegerField(help_text='Time in minutes for show the image.', default=1)


class Propaganda(models.Model):
	types = (
	    ('video', 'Video'),
		('image', 'Images'),
	)
	choice   = models.CharField(max_length=10, choices=types, default="video")
	video    = models.FileField(upload_to="videos/", blank=True, default="")
	images   = models.ManyToManyField(Image)	

	def __unicode__(self):
		return "%d:  %s" % (self.pk, self.choice)	
