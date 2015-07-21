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

def search(request) :
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['directions', 'name',])
        
        found_entries = Recipes.objects.filter(entry_query).order_by('name')

    length = 0
    final_dict = {'d':found_entries,'query': query_string, 'length': length}
    return render_to_response('search.html', {'d': found_entries}, context_instance=RequestContext(request))

#def search(request):
#    query_string = ''
#    found_entries = None
#    results = {}
#
#    rfields = ['name','recipe_id','directions','nut_info','quant_data']
#    ifields = ['ing_id','name','quant_data','nut_info']
#    cfields = ['id_cusine','name','quant_data','ingr','reci']
#    allfields = [rfields, ifields, cfields]
#
#    dprint(request.GET)
#    if ('q' in request.GET) :
#        query_string = request.GET['q']
#        dprint("query string is "+str(query_string))
#
#        rfound_and = submit_requests(query_string, Recipes, rfields, 1)
##        ifound_and = submit_requests(query_string, Ingredients, ifields, 1)
##        cfound_and = submit_requests(query_string, Cuisines, cfields, 1)
#
#        rfound_or = submit_requests(query_string, Recipes, rfields, 0)
##        ifound_or = submit_requests(query_string, Ingredients, ifields, 0)
##        cfound_or = submit_requests(query_string, Cuisines, cfields, 0)
#        
#        print("found_and recipes: "+str(rfound_and))
##        print("found_and ingredients: "+str(ifound_and))
##        print("found_and cuisines: "+str(cfound_and))
#
#        print("found_or recipes: "+str(rfound_or))
##        print("found_or ingredients: "+str(ifound_or))
##        print("found_or cuisines: "+str(cfound_or))
#        
##        or_results = { 'query_string': query_string, 'found_or_recipes': rfound_or, 'found_or_ingredients': ifound_or, 'found_or_cuisines': cfound_or}
#
##        and_results = { 'query_string': query_string, 'found_and_recipes': rfound_and, 'found_and_ingredients': ifound_and, 'found_and_cuisines': cfound_and}
#        #results = { 'query_string': query_string, 'found_recipes': rfound, 'found_ingredients': ifound, 'found_cuisines': cfound}
#    else :
#        results = {}
#        dprint("NOOOOOOO")
#
#    rlen = len(rfound_and)
##    ilen = len(ifound_and)
##    clen = len(cfound_and)
#
#    rlen_or = len(rfound_or)
##    ilen_or = len(ifound_or)
##    clen_or = len(cfound_or)
#
#    length = max(rlen_or, ilen_or, clen_or)
#
#    #Zip snippets here
#    #lengthOfResults = len(results)
#    snippets = {}
#    results = zip(results,snippets)
#    print("AND RESULTS")
#    dprint(str(and_results))
#    print("OR RESULTS")
#    dprint(str(or_results))
#
#    final_dict = {'d':results,'query': query_string, 'length': length}
#    print(str(final_dict))
#    return render_to_response('search.html',final_dict, context_instance=RequestContext(request))  
#
#
#
#def submit_requests(query_string, model, fieldlist, both):
#    query = []
#    idx = 0
#    found = []
#    for field in fieldlist :
#        query += [get_query(both, query_string, [field])]
##        if model == 'Recipes':
#        found = Recipes.objects.filter(query[idx]).order_by('name')
##        if model == 'Ingredients':
##            found += Ingredients.objects.filter(query[idx]).order_by('name')
##        if model == 'Cuisines':
##            found += Cuisines.objects.filter(query[idx]).order_by('name')
#        idx = idx + 1
#    return found


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
 
  
    






