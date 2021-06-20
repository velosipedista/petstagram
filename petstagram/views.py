from django.http.request import HttpRequest
from django.http.response import HttpResponse

def test(req):
    return HttpResponse('iT wOrKs !!!')