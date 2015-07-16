#Test for models.py
import os
import sys
import json
import django.test
from django.test.utils import setup_test_environment
from django.test import TestCase
from django.test import RequestFactory
from django.core.urlresolvers import reverse
from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase

#from django.utils import unittest
import unittest
from django.http import HttpResponse

from json import dumps, loads
#from django.contrib.auth.models import Recipes, Ingredients, Cuisines
from django.contrib.auth.models import *

#TODO : WHAT DOES THIS DO
#from .views import my_view

from foodApp.models import *

    #---------------------
    # Testing the API
    #---------------------

## taken directly from Django RequestFactory documentation:
#class AccountTests(APITestCase):
#   def test_create_recipe(self):
#      url = reverse('recipes')
#      data = {'name': 'foodApp'}
#      response = self.client.post(url, data, format='json')
#      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#      self.assertEqual(response.data, data)


class ModelTestCase(TestCase):

	#---------------------
	# Recipe Model
	#---------------------

   def test_recipes_model1(self):

      test_cuisine = {
         "id": 2,
         "id_cusine": "american",
         "name": "American",
         "url": "",
         "quant_data": "{'diversity': 29.256198347107436, 'diveristy': 29.256198347107436, 'popularity': 11.4, 'number_of_recipes': 57, 'number_of_ingredients': 177, 'avg_salt': 294.8794827586207}",
         "ingr": "{'veal-calves-liver': ['veal calves liver', 'veal-calves-liver'], 'cardamom-seed-ground': ['ground cardamom seed', 'cardamom-seed-ground']}",
         "reci": "{'poppy-seed-dressing': ['Poppy Seed Dressing', 'poppy-seed-dressing'], 'home-style-meatloaf': ['Home-Style Meatloaf', 'home-style-meatloaf']}"
      }
      test_ingredients = {
         "id": 229,
         "ing_id": "oil-peanut",
         "name": "peanut oil",
         "quant_data": "{'diveristy': 6.0606060606060606, 'number_of_recipes': 2, 'popularity': 0.4, 'calories_per_100g': 884.0, 'number_of_cuisines': 2}",
         "nut_info": "{'protein': '0.0 g per 100g ', 'carbohydrates': '0.0 g per 100g ', 'saturated fat': '16.9 g per 100g ', 'fat': '100.0 g per 100g ', 'iron': '0.03 mg per 100g ', 'calories from fat': '900.0 kcal per 100g ', 'trans fat': '0.0 g per 100g ', 'cholesterol': '0.0 mg per 100g ', 'calories': '884.0 kcal per 100g ', 'vitamin a': '0.0 IU per 100g ', 'vitamin c': '0.0 mg per 100g ', 'calcium': '0.0 mg per 100g ', 'sodium': '0.0 mg per 100g '}",
         "all_cuisines": "{'n-a': ['N/A', 'n-a'], 'american-southern': ['American: Southern', 'american-southern']}",
         "all_recipes": "{'lemongrass-oil': ['Lemongrass Oil', 'lemongrass-oil'], 'mopping-sauce': ['Mopping Sauce', 'mopping-sauce']}"
      }
   
      Cuisines.objects.create(**test_cuisine)
      Ingredients.objects.create(**test_ingredients)
      c = Cuisines.objects.get(name = test_cuisine["name"])
      i = Ingredients.objects.get(ing_id = test_ingredients["ing_id"])
      test_recipe = {
         "name": "Flaky Pie Dough Shell",
         "recipe_id": "flaky-pie-dough-shell",
         "directions": "SHAPING CRUSTS  Crusts are shaped by rolling out the dough to fit into a pie pan or tart shell (mold) or to sit on top of fillings. Mealy, flaky and sweet doughs are all easier to roll out and work with if well chilled, as chilling keeps the fat firm and prevents stickiness. When rolling and shaping the dough, work on a clean, flat surface (wood or marble is best). Lightly dust the work surface, rolling pin and dough with pastry flour before starting to roll the dough. Also, work only with a manageable amount at a time: usually one crusts worth for a pie or standard-sized tart or enough for 10 to 12 tartlet shells. ",
         "ingredient_amount": "{'flaky-pie-dough': ['Flaky Pie Dough', '2, 10 lb', 'flaky-pie-dough']}",
         "img": "https://api.pearson.com/kitchen-manager/v1/images/full/defaultrecipe.jpg",
         "nut_info": "{'sodium': '1632.4 mg per 100g ', 'cholesterol': '325.92 mg per 100g ', 'trans fat': '0 g per 100g ', 'carbohydrates': '164.92 g per 100g ', 'calories from fat': '1136.52 g per 100g ', 'protein': '26.46 g per 100g ', 'saturated fat': '78.26 g per 100g ', 'calories': '1841.56 kcal per 100 ', 'calcium': '162.4 mg per 100g ', 'iron': '9.52 mg per 100g ', 'fat': '126.28 g per 100g ', 'vitamin c': '0.42 mg per 100g ', 'vitamin a': '3879.68 IU per 100g '}",
         "quant_data": "{'price': 3.49, 'number_of_ingredients': 1, 'total_fat': 203.54000000000002, 'calories_per_100g': 1841.56, 'Serves': 3, 'yields': 'Yields 3 ea'}",
         "cuisine_ori": "['American', 'american']",
      }
      test_recipe["cuisine"] = c

      
      Recipes.objects.create(**test_recipe)
      recipe_get = Recipes.objects.get(id = 1)
      recipe_get.ingredients.add(i)
      self.assertEqual(recipe_get.id, 1)
      self.assertEqual(recipe_get.name, "Flaky Pie Dough Shell")
      self.assertEqual(recipe_get.recipe_id, "flaky-pie-dough-shell")
      self.assertEqual(recipe_get.directions, "SHAPING CRUSTS  Crusts are shaped by rolling out the dough to fit into a pie pan or tart shell (mold) or to sit on top of fillings. Mealy, flaky and sweet doughs are all easier to roll out and work with if well chilled, as chilling keeps the fat firm and prevents stickiness. When rolling and shaping the dough, work on a clean, flat surface (wood or marble is best). Lightly dust the work surface, rolling pin and dough with pastry flour before starting to roll the dough. Also, work only with a manageable amount at a time: usually one crusts worth for a pie or standard-sized tart or enough for 10 to 12 tartlet shells. ")
      self.assertEqual(recipe_get.cuisine,c )
      self.assertEqual(recipe_get.ingredient_amount, "{'flaky-pie-dough': ['Flaky Pie Dough', '2, 10 lb', 'flaky-pie-dough']}")
      self.assertEqual(recipe_get.img, "https://api.pearson.com/kitchen-manager/v1/images/full/defaultrecipe.jpg")
      self.assertEqual(recipe_get.nut_info, "{'sodium': '1632.4 mg per 100g ', 'cholesterol': '325.92 mg per 100g ', 'trans fat': '0 g per 100g ', 'carbohydrates': '164.92 g per 100g ', 'calories from fat': '1136.52 g per 100g ', 'protein': '26.46 g per 100g ', 'saturated fat': '78.26 g per 100g ', 'calories': '1841.56 kcal per 100 ', 'calcium': '162.4 mg per 100g ', 'iron': '9.52 mg per 100g ', 'fat': '126.28 g per 100g ', 'vitamin c': '0.42 mg per 100g ', 'vitamin a': '3879.68 IU per 100g '}")
      self.assertEqual(recipe_get.quant_data, "{'price': 3.49, 'number_of_ingredients': 1, 'total_fat': 203.54000000000002, 'calories_per_100g': 1841.56, 'Serves': 3, 'yields': 'Yields 3 ea'}")
      self.assertEqual(recipe_get.cuisine_ori, "['American', 'american']")
