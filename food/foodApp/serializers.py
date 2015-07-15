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
           'ingredient_amount',
           'img',
           'nut_info',
           'quant_data',
           'cuisine_ori'
            )

class IngredientsSerializer(serializers.ModelSerializer) : 
    class Meta: 
        model = Ingredients
        fields = (
            'id',
            'ing_id', 
            'name',
            'quant_data', 
            'nut_info',
            'all_cuisines',
            'all_recipes'
            )

class CuisinesSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Cuisines
        fields = (
            'id',
            'id_cusine',
            'name',
            'url',
            'quant_data',
            'ingr',
            'reci'
            )


 
