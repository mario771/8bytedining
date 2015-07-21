from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework import generics
from .models import Cuisines, Recipes, Ingredients
from .search import normalize_query, get_query

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
      ingredient_dict['id'] =  ingredient.ing_id
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
    ingredient_dict['id'] =  ingredient.ing_id
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
        cuisine_dict['id'] = cuisine.id_cusine
        cuisine_dict['name'] = cuisine.name
        cuisine_dict['url'] = cuisine.url
        cuisine_dict['quant_data'] = eval(cuisine.quant_data)
        cuisine_dict['recipes'] = eval(cuisine.reci)
        cuisine_dict['ingredients'] = eval(cuisine.ingr)

        context_dict[cuisine.id_cusine] = cuisine_dict

   
    return render_to_response('cuisine_model.html',{'d':context_dict}, context)


     
def cuisine(request, c_name):

    context = RequestContext(request)
    cuisine = Cuisines.objects.get(id_cusine=c_name)

    cuisine_dict = {}
    cuisine_dict['id'] = cuisine.id_cusine
    cuisine_dict['name'] = cuisine.name
    cuisine_dict['url'] = cuisine.url
    cuisine_dict['quant_data'] = eval(cuisine.quant_data)
    cuisine_dict['recipes'] = eval(cuisine.reci)
    cuisine_dict['ingredients'] = eval(cuisine.ingr)

    return render_to_response('cuisine_page.html', {'d':cuisine_dict}, context)

def dprint(a):
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print(str(a))
    print("@@@@@@@@@@@@@@@@@@@@@@")

def search(request):
    query_string = ''
    found_entries = None
    results = {}
    found_recipes = {}
    found_ingredients = {}
    found_cuisines = {}

    #if ('q' in request.GET) and request.GET['q'].strip():
    dprint(request.GET)
    if ('q' in request.GET) :
        query_string = request.GET['q']
        #query_string = request.GET.get('q')
        #query_string = request.GET.get.q
        dprint("query string is "+str(query_string))
        
        recipe_query = get_query(query_string, ['name','recipe_id','directions','nut_info','quant_data'])
        ingredient_query = get_query(query_string, ['ing_id','name','quant_data','nut_info'])
        cuisine_query = get_query(query_string, ['id_cusine','name','quant_data','ingr','reci'])
        
        found_recipes = Recipes.objects.filter(recipe_query).order_by('name')
        found_ingredients = Ingredients.objects.filter(ingredient_query).order_by('name')
        found_cuisines = Cuisines.objects.filter(cuisine_query).order_by('name')
        results = { 'query_string': query_string, 'found_recipes': found_recipes, 'found_ingredients': found_ingredients, 'found_cuisines': found_cuisines}
    else :
        results = {}
        dprint("NOOOOOOO")

    rlen = len(found_recipes)
    ilen = len(found_ingredients)
    clen = len(found_cuisines)
    length = max(rlen, ilen, clen)

    dprint("found recipes: "+str(found_recipes))
    dprint("found ingredients: "+str(found_ingredients))
    dprint("found cuisines: "+str(found_cuisines))
    #Zip snippets here
    #lengthOfResults = len(results)
    snippets = {}
    results = zip(results,snippets)
#    for i in results :
#        dprint str(i)


    final_dict = {'d':results,'query': query_string, 'length': length}

    print(str(final_dict))

    return render_to_response('search.html',final_dict, context_instance=RequestContext(request))  

def crossFit():

    context = RequestContext(request)

    teamApiUrl = "crossfit.social/"
    requestRegions = urllib.request.urlopen(teamApiUrl+"api/regions/?format=json")
    requestAthletes = urllib.request.urlopen(teamApiUrl+"api/athletes/?format=json")
    requestInstagrams = urlib.request.urlopen(teamApiUrl+"api/instagram/?format=json")

    responseRegions = requestDivisions.read().decode("utf-8")
    regionList = json.loads(responseDivisions)

    responseAthletes = requestAthletes.read().decode("utf-8")
    athleteList = json.loads(responseAthletes)

    responseInstagrams = requestInstagram.read().decode("utf-8")
    instagramList = json.loads(responseInstagrams)



    #this will pass in a list containing an athlete name, region, and an instagram post
    crossFitDict = {}

    #Right now we're getting all the athletes, maybe just a subset?

    for athlete in athleteList :
        crossFitDict['athlete_name'] = athlete.name
        crossFitDict['region'] = regionList[athlete.region] 
        crossFitdict['post'] = instagramList.athlete.id[athlete.id].post 
        #For each athlete have their image pop up in a box along with
        # height and affiliation and weight
        crossFitDict['img'] = athlete.img 
        crossFitDict['height'] = athlete.height
        crossFitDict['weight'] = athlete.weight



    return render_to_response('crossFit.html', {'d': crossFitDict}, context)
 
  
    






