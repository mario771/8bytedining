from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework import generics


def home(request):
   context = RequestContext(request)
   return render_to_response('8byte_splash.html',context)

def about (request) :
   context = RequestContext(request)
   return render_to_response('about.html',context)

def model (request) :
  context = RequestContext(request)
  return render_to_response('model.html',context)

def recipe_page (request) :
   context = RequestContext(request)
   return render_to_response('recipe_page.html',context)

def ingredient_page (request) :
   context = RequestContext(request)
   return render_to_response('ingredient_page.html',context)

def cuisine_page (request) :
   context = RequestContext(request)
   return render_to_response('cuisine_page.html',context)





#def recipes(request): 

   #Implement try except block later  

 #  context = RequestContext(request)
 #  recipes = Recipes.objects.all.order_by('name')





