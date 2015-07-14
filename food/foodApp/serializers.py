from rest_framework import serializers
from models import Recipes, Ingredients, Cuisines

class RecipesSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Recipes 
        field = (id,name,recipe_id,directions, cuisine, ingredients,img,nut_info,quant_dat)

class IngredientsSerializer(serializers.ModelSerializer) : 
    class Meta: 
        model = Ingredients
        field = (id,ing_id,name,recipe_count,quant_data,nut_info)

class CuisinesSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Cuisines
        field = (id,cuisine,name,url,recipe_count,quant_data)


 
