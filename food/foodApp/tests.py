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
            

            
    def test_cuisine_model1(self):
        Cuisine.objects.create(name="French", id="french", url="https://api.pearson.com/kitchen-manager/v1/cuisines/french", recipes="", ingredients="", recipe_count=158) 

        self.assertEqual(cuisine_get.name,"French")
        self.assertEqual(cuisine_get.cuisine_id,"french")
        self.assertEqual(cuisine_get.url,"https://api.pearson.com/kitchen-manager/v1/cuisines/french")
        self.assertEqual(cuisine_get.recipes,"")
        self.assertEqual(cuisine_get.ingredients,"")
        self.assertEqual(cuisine_get.recipe_count,158) 


    def test_cuisine_model2(self):
        Cuisine.objects.create(name="Italian", id="italian", url="https://api.pearson.com/kitchen-manager/v1/cuisines/italian", recipes="", ingredients="", recipe_count=17) 
        self.assertEqual(cuisine_get.name,"Italian")
        self.assertEqual(cuisine_get.cuisine_id,"italian")
        self.assertEqual(cuisine_get.url,"https://api.pearson.com/kitchen-manager/v1/cuisines/italian")
        self.assertEqual(cuisine_get.recipes,"")
        self.assertEqual(cuisine_get.ingredients,"")
        self.assertEqual(cuisine_get.recipe_count,17 )

    def test_cuisine_model3(self):
        Cuisine.objects.create(name="Mexican", id="mexican", url="https://api.pearson.com/kitchen-manager/v1/cuisines/mexican", recipes="", ingredients="", recipe_count=16) 
        self.assertEqual(cuisine_get.name,"Mexican")
        self.assertEqual(cuisine_get.cuisine_id,"mexican")
        self.assertEqual(cuisine_get.url,"https://api.pearson.com/kitchen-manager/v1/cuisines/mexican")
        self.assertEqual(cuisine_get.recipes,"")
        self.assertEqual(cuisine_get.ingredients,"")
        self.assertEqual(cuisine_get.recipe_count,16 )

    def test_cuisine_model4(self):
        Cuisine.objects.create(name="Indian", id="indian", url="https://api.pearson.com/kitchen-manager/v1/cuisines/indian", recipes="", ingredients="", recipe_count=12) 
        self.assertEqual(cuisine_get.name,"Indian")
        self.assertEqual(cuisine_get.cuisine_id,"indian")
        self.assertEqual(cuisine_get.url,"https://api.pearson.com/kitchen-manager/v1/cuisines/indian")
        self.assertEqual(cuisine_get.recipes,"")
        self.assertEqual(cuisine_get.ingredients,"")
        self.assertEqual(cuisine_get.recipe_count,12 )

    def test_cuisine_model5(self):
        Cuisine.objects.create(name="American: Southern", id="american-southern", url="https://api.pearson.com/kitchen-manager/v1/cuisines/american-southern", recipes="", ingredients="", recipe_count=9)
        self.assertEqual(cuisine_get.name,"American: Southern")
        self.assertEqual(cuisine_get.cuisine_id,"american-southern")
        self.assertEqual(cuisine_get.url,"https://api.pearson.com/kitchen-manager/v1/cuisines/american-southern")
        self.assertEqual(cuisine_get.recipes,"")
        self.assertEqual(cuisine_get.ingredients,"")
        self.assertEqual(cuisine_get.recipe_count,9)

    def test_ingredients_model2(self):
    def test_ingredients_model2(self):
    def test_ingredients_model2(self):
            
# Create your tests here.
