from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
   context = RequestContext(request)
   return render_to_response('8byte_splash.html',context)

def CuisinesModel (request) :
   context = RequestContext(request)
   return render_to_response('CuisineModel.html',context)

def IngredientsModel (request) :
   context = RequestContext(request)
   return render_to_response('IngredientModel.html',context)

def RecipesModel (request) :
   context = RequestContext(request)
   return render_to_response('RecipeModel.html',context)

def Ingredients (request) :
   context = RequestContext(request)
   return render_to_response('Ingredients.html',context)

def Cuisines (request) :
   context = RequestContext(request)
   return render_to_response('Cuisines.html',context)

def Recipes (request) :
   context = RequestContext(request)
   return render_to_response('Recipes.html',context)