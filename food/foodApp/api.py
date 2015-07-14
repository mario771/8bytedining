from .models import Recipes, Ingredients, Cuisines 
from .serializers import RecipesSerializer, IngredientsSerializer, CuisinesSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class RecipeList(APIView): 

   def get(self,request,format=None):
      recipes = Recipes.objects.filter(active=True)
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



