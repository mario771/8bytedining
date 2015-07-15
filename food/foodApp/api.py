from .models import Recipes, Ingredients, Cuisines 
from .serializers import RecipesSerializer, IngredientsSerializer, CuisinesSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class RecipeList(APIView): 

   def get(self,request,format=None):
      recipes = Recipes.objects.filter()
      serialized_recipes = RecipesSerializer(recipes,many=True)
      return Response(serialized_recipes.data)

class RecipeDetail(APIView): 
  
   def get_object(self,pk):
      try:
         return Recipes.objects.get(pk=pk)
      except Recipes.DoesNotExist :  
         raise Http404

   def get(self,request,pk,format=None):
      recipe = self.get_object(pk)
      serialized_recipe = RecipesSerializer(recipe)
      return Response(serialized_recipe.data)

class CuisineList(APIView):

   def get(self,request,format=None):
      cuisines = Cuisines.objects.filter()
      serialized_cuisines = CuisinesSerializer(cuisines,many=True)
      return Response(serialized_cuisines.data)

class CuisineDetail(APIView):

   def get_object(self,pk):
      try:
         return Cuisines.objects.get(pk=pk)
      except Cuisines.DoesNotExist :
         raise Http404

   def get(self,request,pk,format=None):
      cuisine = self.get_object(pk)
      serialized_cuisine = CuisinesSerializer(cuisine)
      return Response(serialized_cuisine.data)


class IngredientList(APIView):

   def get(self,request,format=None):
      ingredients = Ingredients.objects.filter()
      serialized_ingredients = IngredientsSerializer(ingredients,many=True)
      return Response(serialized_ingredients.data)

class IngredientDetail(APIView):

   def get_object(self,pk):
      try:
         return Ingredients.objects.get(pk=pk)
      except Ingredients.DoesNotExist :
         raise Http404

   def get(self,request,pk,format=None):
      ingredient = self.get_object(pk)
      serialized_ingredient = IngredientsSerializer(ingredient)
      return Response(serialized_ingredient.data)


