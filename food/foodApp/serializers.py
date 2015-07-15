from rest_framework import serializers
from .models import Recipes, Ingredients, Cuisines

class RecipesSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Recipes 
        fields = (
           'id',
           'name',
           'recipe_id',
           'directions',
           'cuisine',
           'ingredients',
           'img',
           'nut_info',
           'quant_data'
            )

class IngredientsSerializer(serializers.ModelSerializer) : 
    class Meta: 
        model = Ingredients
        fields = (
            'id',
            'ing_id', 
            'name',
            'recipe_count',
            'quant_data', 
            'nut_info'
            )

class CuisinesSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Cuisines
        fields = (
            'id',
            'cuisine',
            'name,url',
            'recipe_count',
            'quant_data'
            )


 
