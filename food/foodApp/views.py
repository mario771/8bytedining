from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request) :
   return HttpResponse("Hello, world. You're at the food index.")

def potroast (request) :
   context = RequestContext(request)
   return render_to_response('auntruthiespotroast.html',context)
