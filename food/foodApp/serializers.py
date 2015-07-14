from rest_framework import serializers
from models import Recipes, Ingredients, Cuisines

class RecipesSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Recipes 
        field = (id,img,name,nut_info,directions,quant_data,ingrediennts,cuisine,recipe_id)

class IngredientsSerializer(serializers.ModelSerializer) : 
    class Meta: 
        model = Ingredients
        field = (id,ingredient_id,recipe_count,quant_data,name,nut_info)

class CuisinesSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Cuisines
        field = (id,name,cuisine_id,url,recipe_count,quant_data)


 
