import json
import logging

from django.contrib import admin
from django.http import HttpResponse, JsonResponse

logger = logging.getLogger(__name__)

def app_list_view(request):
    data = admin.site.get_app_list(request)

    return JsonResponse(data, safe=False)
