from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import service
import json
# Create your views here.


def index(request):
    template = loader.get_template('vdl/index.html')
    context = {
        'test': 1
    }
    return HttpResponse(template.render(context, request))


def detail(request):
    vhs = service.VideoHistoryService()
    lists = vhs.execList(request.GET.get('url'))
    return HttpResponse(lists)


def live(request):
    template = loader.get_template('vdl/live.html')
    context = {
        'test': 1
    }
    return HttpResponse(template.render(context, request))


def live_urls(request):
    urls = service.LiveUrlService().get_urls(request.GET.get('id'))
    print(urls)
    return HttpResponse(json.dumps(urls), content_type='application/json')

