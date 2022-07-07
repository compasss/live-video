import json
import re

from django.http import HttpResponse
from django.template import loader
from .models import AohsFile
import requests


def index(request):
    template = loader.get_template('txbed/index.html')
    file_list = AohsFile.objects.order_by('-id')
    for it in file_list:
        print(re.search('image', it.content_type))
        it.isImage = re.search('image', it.content_type) is not None
        it.json = json.dumps(it.extra)
    context = {
        'file_list': file_list
    }
    return HttpResponse(template.render(context, request))


def upload(request):
    file = request.FILES['file']
    res = requests.post('https://acloud.aierchina.com:5310/aohsapp/files/upload', files={'file': file}, headers={
        'eyeJwt': request.headers['eyeJwt']
    })
    body = res.json()
    if res.status_code == 200:
        q = AohsFile(file_name=body.get('fileName'), url=body.get('url'), content_type=file.content_type, extra=body)
        q.save()
    return HttpResponse(json.dumps(body), content_type='application/json', status=res.status_code)
