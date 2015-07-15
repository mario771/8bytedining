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

def recipes(request) : 
   context = RequestContext(request)
   recipes = Recipes.objects.all()
   
   context_dict = {}

   for recipe in recipes :
     recipe_dict = {}
     recipe_dict['name'] = recipe.name
     recipe_dict['id'] = recipe.recipe_id
     recipe_dict['cuisine'] = eval(recipe.cuisine_ori)
     recipe_dict['img'] = recipe.img
     recipe_dict['quant_data'] = eval(recipe.quant_data)
     recipe_dict['directions'] = recipe.directions
     recipe_dict['ingredients'] = eval(recipe.ingredient_amount)
     recipe_dict['nut_info'] = eval(recipe.nut_info)
     
     context_dict[recipe.recipe_id] = recipe_dict
 
     
   return render_to_response('recipe_model.html',{'d': context_dict}, context)

   
def recipe(request, r_name):

   context = RequestContext(request)
   recipe = Recipes.objects.get(recipe_id=r_name)
   recipe_dict = {}
   recipe_dict['name'] = recipe.name
   recipe_dict['id'] = recipe.recipe_id
   
   recipe_dict['cuisine'] = eval(recipe.cuisine_ori)
   recipe_dict['img'] = recipe.img
   recipe_dict['quant_data'] = eval(recipe.quant_data)
   
   recipe_dict['directions'] = recipe.directions
   recipe_dict['ingredients'] = eval(recipe.ingredient_amount)
   recipe_dict['nut_info'] = eval(recipe.nut_info) 
 
   return render_to_response('recipe_page.html', {'d': recipe_dict}, context)

def ingredients(request) : 
   context = RequestContext(request)
   ingredients = Ingredients.objects.all()
   
   context_dict = {}
  
   for ingredient in ingredients :
      ingredient_dict = {}
      ingredient_dict['ing_id'] =  ingredient.ing_id
      ingredient_dict['name'] = ingredient.name
      ingredient_dict['quant_data'] = eval(ingredient.quant_data)
      ingredient_dict['nut_info'] = eval(ingredient.nut_info)
      ingredient_dict['recipes'] = eval(ingredient.all_recipes)
      ingredient_dict['cuisines'] = eval(ingredient.all_cuisines)
 
      context_dict[ingredient.ing_id] = ingredient_dict
 
   return render_to_response('ingredient_model.html',{'d': context_dict}, context)

  
   
def ingredient(request, i_name):

   context = RequestContext(request)
   ingredient = Ingredients.objects.get(ing_id=i_name)
   
   ingredient_dict = {}
   ingredient_dict['ing_id'] =  ingredient.ing_id
   ingredient_dict['name'] = ingredient.name
   ingredient_dict['quant_data'] = eval(ingredient.quant_data)
   ingredient_dict['nut_info'] = eval(ingredient.nut_info)
   ingredient_dict['recipes'] = eval(ingredient.all_recipes)
   ingredient_dict['cuisines'] = eval(ingredient.all_cuisines)

   return render_to_response('ingredient_page.html',{'d':ingredient_dict}, context)
   

def cuisines(request) : 
   context = RequestContext(request)
   cuisines = Cuisines.objects.all()
   context_dict = {}   

   for cuisine in cuisines: 
       cuisine_dict = {}
       cuisine_dict['id_cuisine'] = cuisine.id_cusine
       cuisine_dict['name'] = cuisine.name
       cuisine_dict['url'] = cuisine.url
       cuisine_dict['quant_data'] = eval(cuisine.quant_data)
       cuisine_dict['recipes'] = eval(cuisine.reci)
       cuisine_dict['ingredients'] = eval(cuisine.ingr)
   
       context_dict[cuisine.id_cuisine] = cuisine_dict

   
    return render_to_response('cuisine_page.html',{'d':context_dict}, context)


     
def cuisine(request, c_name):

   context = RequestContext(request)
   cuisine = Cuisines.objects.get(id_cusine=c_name)
  
   cuisine_dict = {}
   cuisine_dict['id_cuisine'] = cuisine.id_cusine
   cuisine_dict['name'] = cuisine.name
   cuisine_dict['url'] = cuisine.url
   cuisine_dict['quant_data'] = eval(cuisine.quant_data)
   cuisine_dict['recipes'] = eval(cuisine.reci)
   cuisine_dict['ingredients'] = eval(cuisine.ingr)

   return render_to_response('cuisine_page.html', {'d':cuisine_dict}, context)
