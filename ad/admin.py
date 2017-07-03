# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Image, Propaganda

class ImageInline(admin.StackedInline):
    model = Propaganda.images.through

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	pass

@admin.register(Propaganda)
class PropagandaAdmin(admin.ModelAdmin):
	inlines = [ImageInline,]
	exclude = ('images',)
