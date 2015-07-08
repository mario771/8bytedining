#Test for models.py
import os
import sys
import json
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse
from django.core.management import call_command

from django.utils import unittest
from django.test import TestCase
from django.http import HttpResponse

from json import dumps, loads

from models.py import *

class ModelTestCase(TestCase):

	#---------------------
	# Recipe Model
	#---------------------

	def test_recipes_model1(self):
            Recipes.objects.create(name= 'Irish Soda Bread', recipe_id = 'Irish Soda Bread', url ="https://api.pearson.com/kitchen-manager/v1/recipes/irish-soda-bread", directions = 'Soak the currants in the whiskey until plump, at least 1 hour. Sift the dry ingredients together. Stir in the currants and whiskey. Stir in the buttermilk, making a stiff batter. Spread the batter in a greased 8-inch (20-centimeter) round cake pan. Bake at 350Â°F (180Â°C) until well browned and firm, approximately 30 minutes.', nutritionalInfo =""  , cuisineGivenRecipe = "British Isles", ingredients ="salt"  )
            recipe_get = Recipes.objects.get(name= "Irish Soda Bread")
            self.assertEqual(recipe_get.name, "Irish Soda Bread")
            self.assertEqual(recipe_get.url, "https://api.pearson.com/kitchen-manager/v1/recipes/irish-soda-bread")
            self.assertEqual(recipe_get.directions, 'Soak the currants in the whiskey until plump, at least 1 hour. Sift the dry ingredients together. Stir in the currants and whiskey. Stir in the buttermilk, making a stiff batter. Spread the batter in a greased 8-inch (20-centimeter) round cake pan. Bake at 350Â°F (180Â°C) until well browned and firm, approximately 30 minutes.')
            self.assertEqual(recipe_get.nutritionalInfo, "")
            self.assertEqual(recipe_get.cuisineGivenRecipe, "British Isles")
            self.assertEqual(recipe_get.ingredients, "salt")

        def test_recipes_model2(self):
            Recipes.objects.create(name= "Almond Cream", recipe_id = "Almond Cream", url ="https://api.pearson.com/kitchen-manager/v1/recipes/almond-cream", directions = "Cream the butter and sugar. Slowly add the eggs, scraping down the bowl as necessary. Stir the flour and almonds together, then add to the butter mixture. Blend until no lumps re-main. Almond cream may be stored under refrigeration for up to 3 weeks. ", nutritionalInfo =""  , cuisineGivenRecipe = "French", ingredients ="eggs"  )
            recipe_get = Recipes.objects.get(name= "Almond Cream")
            self.assertEqual(recipe_get.name, "Almond Cream")
            self.assertEqual(recipe_get.url, "https://api.pearson.com/kitchen-manager/v1/recipes/almond-cream")
            self.assertEqual(recipe_get.directions, "Cream the butter and sugar. Slowly add the eggs, scraping down the bowl as necessary. Stir the flour and almonds together, then add to the butter mixture. Blend until no lumps re-main. Almond cream may be stored under refrigeration for up to 3 weeks. ")
            self.assertEqual(recipe_get.nutritionalInfo, "")
            self.assertEqual(recipe_get.cuisineGivenRecipe, "French")
            self.assertEqual(recipe_get.ingredients, "eggs")

        def test_recipes_model3(self):
            Recipes.objects.create(name= 'Irish Soda Bread', recipe_id = 'Irish Soda Bread', url ="https://api.pearson.com/kitchen-manager/v1/recipes/irish-soda-bread", directions = 'Soak the currants in the whiskey until plump, at least 1 hour. Sift the dry ingredients together. Stir in the currants and whiskey. Stir in the buttermilk, making a stiff batter. Spread the batter in a greased 8-inch (20-centimeter) round cake pan. Bake at 350Â°F (180Â°C) until well browned and firm, approximately 30 minutes.', nutritionalInfo =""  , cuisineGivenRecipe = "British Isles", ingredients ="salt"  )
            recipe_get = Recipes.objects.get(name= "Irish Soda Bread")
            self.assertEqual(recipe_get.name, "Irish Soda Bread")
            self.assertEqual(recipe_get.url, "https://api.pearson.com/kitchen-manager/v1/recipes/irish-soda-bread")
            self.assertEqual(recipe_get.directions, 'Soak the currants in the whiskey until plump, at least 1 hour. Sift the dry ingredients together. Stir in the currants and whiskey. Stir in the buttermilk, making a stiff batter. Spread the batter in a greased 8-inch (20-centimeter) round cake pan. Bake at 350Â°F (180Â°C) until well browned and firm, approximately 30 minutes.')
            self.assertEqual(recipe_get.nutritionalInfo, "")
            self.assertEqual(recipe_get.cuisineGivenRecipe, "British Isles")
            self.assertEqual(recipe_get.ingredients, "salt")
            
            
            
# Create your tests here.
