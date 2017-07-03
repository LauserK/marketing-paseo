# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Propaganda, Image
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def APIResponse(data, message, success):
    """
    Utilidad para responder la peticion con una respuesta en json
    """
    settings = {
        "success": success,
        "message": message
    }
    if data is not None:
        return JsonResponse({"data": data, "settings":settings})
    else:
        return JsonResponse({"data": [], "settings": settings})

class getAd(View):
	def get(self, request):
		pk = request.GET.get('pk')	

		try:
			ad = Propaganda.objects.get(pk=pk)
		except ObjectDoesNotExist:
			return APIResponse("", "Ad doesn't exists!", 0)

		if ad.choice == "video":
			data = [{
				"type": ad.choice,
				"video_url": ad.video.url
			}]
			return APIResponse(data, "GetAd", 1)

		elif ad.choice == "image":
			images = list(ad.images.all().values())
			d = 0
			for i in images:
				images[d]['file'] = settings.MEDIA_URL + images[d]['file']
				d+=1


			data = [{
				"type": ad.choice,
				"images": images
			}]
			return APIResponse(data, "GetAd", 1)

		