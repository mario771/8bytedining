from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework import generics
from .models import Cuisines, Recipes, Ingredients

def home(request):
   context = RequestContext(request)
   return render_to_response('8byte_splash.html',context)

def about (request) :
   context = RequestContext(request)
   return render_to_response('about.html',context)

"""
def recipe_page (request) :
   context = RequestContext(request)
   return render_to_response('recipe_page.html',context)

def ingredient_page (request) :
   context = RequestContext(request)
   return render_to_response('ingredient_page.html',context)

def cuisine_page (request) :
   context = RequestContext(request)
   return render_to_response('cuisine_page.html',context)
"""

def recipes(request) : 
   context = RequestContext(request)
   recipes = Recipes.objects.all()
   
   rlist = [r.recipe_id for r in recipes ]
   z = zip(recipes,rlist)
  # recipes = Recipes.objects.raw('SELECT * FROM "foodApp_recipes"')
   context_dict = {
     'title': 'Recipes',
     'wow_urls' : z
     }
     
   return render_to_response('recipes.html', context_dict, context)


   
def recipe(request, r_name):
# nut_info, quant_data
   context = RequestContext(request)
   recipe = Recipes.objects.get(recipe_id=r_name)
   recipe_dict = {}
   recipe_dict['name'] = recipe.name
   recipe_dict['id'] = recipe.recipe_id
   
   recipe_dict['cuisine'] = recipe.cuisine
   recipe_dict['img'] = recipe.img
   recipe_dict['quant_data'] = eval(recipe.quant_data)
   recipe_dict['directions'] = recipe.directions
   recipe_dict['ingredients'] = eval(recipe.ingredient_amount)

 #  return render_to_response('recipes.html', context_dict, context)
   return render_to_response('recipe_page.html', {'d': recipe_dict}, context)

def ingredients(request) : 
   context = RequestContext(request)
   ingredients = Ingredients.objects.all()
   
   rlist = [r.ingredient_id for r in ingredients ]
   z = zip(ingredients,rlist)

  # ingredients = Ingredients.objects.raw('SELECT * FROM "foodApp_ingredients"')
   context_dict = {
     'title': 'Ingredients',
     'wow_urls' : z
     }
   
def ingredient(request, r_name):
   context = RequestContext(request)
   ingredient = Country.objects.get(ingredient_id=r_name)

 #  return render_to_response('ingredients.html', context_dict, context)
   return render_to_response('ingredients.html', context_dict, context)


def cuisines(request) : 
   context = RequestContext(request)
   cuisines = Cuisines.objects.all()
   
   rlist = [c.cuisine_id for c in cuisines ]
   z = zip(cuisines,clist)

  # cuisines = Cuisines.objects.raw('SELECT * FROM "foodApp_cuisines"')
   context_dict = {
     'title': 'Cuisines',
     'wow_urls' : z
     }
   
def cuisine(request, c_name):
   context = RequestContext(request)
   cuisine = Country.objects.get(cuisine_id=c_name)

 #  return render_to_response('cuisines.html', context_dict, context)
   return render_to_response('cuisines.html', context_dict, context)
