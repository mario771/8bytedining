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
from django.contrib.auth.models import *

from foodApp.models import *


class ModelTestCase(TestCase):

    def test_recipes_model1(self):

        test_cuisine = {
            'id': 2,
            'id_cusine': 'american',
            'name': 'American',
            'url': '',
            'quant_data': "{'diversity': 29.256198347107436, 'diveristy': 29.256198347107436, 'popularity': 11.4, 'number_of_recipes': 57, 'number_of_ingredients': 177, 'avg_salt': 294.8794827586207}",
            'ingr': "{'veal-calves-liver': ['veal calves liver', 'veal-calves-liver'], 'cardamom-seed-ground': ['ground cardamom seed', 'cardamom-seed-ground']}",
            'reci': "{'poppy-seed-dressing': ['Poppy Seed Dressing', 'poppy-seed-dressing'], 'home-style-meatloaf': ['Home-Style Meatloaf', 'home-style-meatloaf']}",
            }
        test_ingredients = {
            'id': 229,
            'ing_id': 'oil-peanut',
            'name': 'peanut oil',
            'quant_data': "{'diveristy': 6.0606060606060606, 'number_of_recipes': 2, 'popularity': 0.4, 'calories_per_100g': 884.0, 'number_of_cuisines': 2}",
            'nut_info': "{'protein': '0.0 g per 100g ', 'carbohydrates': '0.0 g per 100g ', 'saturated fat': '16.9 g per 100g ', 'fat': '100.0 g per 100g ', 'iron': '0.03 mg per 100g ', 'calories from fat': '900.0 kcal per 100g ', 'trans fat': '0.0 g per 100g ', 'cholesterol': '0.0 mg per 100g ', 'calories': '884.0 kcal per 100g ', 'vitamin a': '0.0 IU per 100g ', 'vitamin c': '0.0 mg per 100g ', 'calcium': '0.0 mg per 100g ', 'sodium': '0.0 mg per 100g '}",
            'all_cuisines': "{'n-a': ['N/A', 'n-a'], 'american-southern': ['American: Southern', 'american-southern']}",
            'all_recipes': "{'lemongrass-oil': ['Lemongrass Oil', 'lemongrass-oil'], 'mopping-sauce': ['Mopping Sauce', 'mopping-sauce']}",
            }

        Cuisines.objects.create(**test_cuisine)
        Ingredients.objects.create(**test_ingredients)
        c = Cuisines.objects.get(name=test_cuisine['name'])
        i = Ingredients.objects.get(ing_id=test_ingredients['ing_id'])
        test_recipe = {
            'name': 'Flaky Pie Dough Shell',
            'recipe_id': 'flaky-pie-dough-shell',
            'directions': 'SHAPING CRUSTS  Crusts are shaped by rolling out the dough to fit into a pie pan or tart shell (mold) or to sit on top of fillings. Mealy, flaky and sweet doughs are all easier to roll out and work with if well chilled, as chilling keeps the fat firm and prevents stickiness. When rolling and shaping the dough, work on a clean, flat surface (wood or marble is best). Lightly dust the work surface, rolling pin and dough with pastry flour before starting to roll the dough. Also, work only with a manageable amount at a time: usually one crusts worth for a pie or standard-sized tart or enough for 10 to 12 tartlet shells. ',
            'ingredient_amount': "{'flaky-pie-dough': ['Flaky Pie Dough', '2, 10 lb', 'flaky-pie-dough']}",
            'img': 'https://api.pearson.com/kitchen-manager/v1/images/full/defaultrecipe.jpg',
            'nut_info': "{'sodium': '1632.4 mg per 100g ', 'cholesterol': '325.92 mg per 100g ', 'trans fat': '0 g per 100g ', 'carbohydrates': '164.92 g per 100g ', 'calories from fat': '1136.52 g per 100g ', 'protein': '26.46 g per 100g ', 'saturated fat': '78.26 g per 100g ', 'calories': '1841.56 kcal per 100 ', 'calcium': '162.4 mg per 100g ', 'iron': '9.52 mg per 100g ', 'fat': '126.28 g per 100g ', 'vitamin c': '0.42 mg per 100g ', 'vitamin a': '3879.68 IU per 100g '}",
            'quant_data': "{'price': 3.49, 'number_of_ingredients': 1, 'total_fat': 203.54000000000002, 'calories_per_100g': 1841.56, 'Serves': 3, 'yields': 'Yields 3 ea'}",
            'cuisine_ori': "['American', 'american']",
            }
        test_recipe['cuisine'] = c

        Recipes.objects.create(**test_recipe)
        recipe_get = Recipes.objects.get(id=1)
        recipe_get.ingredients.add(i)
        self.assertEqual(recipe_get.id, 1)
        self.assertEqual(recipe_get.name, 'Flaky Pie Dough Shell')
        self.assertEqual(recipe_get.recipe_id, 'flaky-pie-dough-shell')
        self.assertEqual(recipe_get.directions,
                         'SHAPING CRUSTS  Crusts are shaped by rolling out the dough to fit into a pie pan or tart shell (mold) or to sit on top of fillings. Mealy, flaky and sweet doughs are all easier to roll out and work with if well chilled, as chilling keeps the fat firm and prevents stickiness. When rolling and shaping the dough, work on a clean, flat surface (wood or marble is best). Lightly dust the work surface, rolling pin and dough with pastry flour before starting to roll the dough. Also, work only with a manageable amount at a time: usually one crusts worth for a pie or standard-sized tart or enough for 10 to 12 tartlet shells. '
                         )
        self.assertEqual(recipe_get.cuisine, c)
        self.assertEqual(recipe_get.ingredient_amount,
                         "{'flaky-pie-dough': ['Flaky Pie Dough', '2, 10 lb', 'flaky-pie-dough']}"
                         )
        self.assertEqual(recipe_get.img,
                         'https://api.pearson.com/kitchen-manager/v1/images/full/defaultrecipe.jpg'
                         )
        self.assertEqual(recipe_get.nut_info,
                         "{'sodium': '1632.4 mg per 100g ', 'cholesterol': '325.92 mg per 100g ', 'trans fat': '0 g per 100g ', 'carbohydrates': '164.92 g per 100g ', 'calories from fat': '1136.52 g per 100g ', 'protein': '26.46 g per 100g ', 'saturated fat': '78.26 g per 100g ', 'calories': '1841.56 kcal per 100 ', 'calcium': '162.4 mg per 100g ', 'iron': '9.52 mg per 100g ', 'fat': '126.28 g per 100g ', 'vitamin c': '0.42 mg per 100g ', 'vitamin a': '3879.68 IU per 100g '}"
                         )
        self.assertEqual(recipe_get.quant_data,
                         "{'price': 3.49, 'number_of_ingredients': 1, 'total_fat': 203.54000000000002, 'calories_per_100g': 1841.56, 'Serves': 3, 'yields': 'Yields 3 ea'}"
                         )
        self.assertEqual(recipe_get.cuisine_ori,
                         "['American', 'american']")

    def test_cuisine_model1(self):
        test_dic = {
            'id': 2,
            'id_cusine': 'american',
            'name': 'American',
            'url': '',
            'quant_data': "{'diversity': 29.256198347107436, 'diveristy': 29.256198347107436, 'popularity': 11.4, 'number_of_recipes': 57, 'number_of_ingredients': 177, 'avg_salt': 294.8794827586207}",
            'ingr': "{'veal-calves-liver': ['veal calves liver', 'veal-calves-liver'], 'cardamom-seed-ground': ['ground cardamom seed', 'cardamom-seed-ground'], 'garlic-clove': ['garlic clove', 'garlic-clove'], 'oil-extra-virgin-olive': ['extra virgin olive oil', 'oil-extra-virgin-olive'], 'mayonnaise': ['mayonnaise', 'mayonnaise'], 'worcestershire-sauce': ['worcestershire sauce', 'worcestershire-sauce'], 'orange-segments': ['Orange Segments', 'orange-segments'], 'eggs-pasteurized': ['pasteurized eggs', 'eggs-pasteurized'], 'broccoli-florets': ['broccoli florets', 'broccoli-florets'], 'lime-juice-fresh': ['Lime Juice (fresh)', 'lime-juice-fresh'], 'horseradish-fresh': ['fresh horseradish', 'horseradish-fresh'], 'oregano-dried-whole': ['dried whole oregano', 'oregano-dried-whole'], 'chicken-stock': ['Chicken Stock', 'chicken-stock'], 'flour-all-purpose': ['all purpose flour', 'flour-all-purpose'], 'corn-fresh': ['fresh corn', 'corn-fresh'], 'coconut-macaroon': ['macaroon coconut', 'coconut-macaroon'], 'egg-yolks': ['egg yolks', 'egg-yolks'], 'croutons': ['Croutonsas needed', 'croutons'], 'vinegar-red-wine': ['red wine vinegar', 'vinegar-red-wine'], 'beef-chuck': ['beef chuck', 'beef-chuck'], 'cream-half-half': ['half & half cream', 'cream-half-half'], 'cinnamon-stick': ['cinnamon stick', 'cinnamon-stick'], 'mustard-whole-grain': ['whole grain mustard', 'mustard-whole-grain'], 'mustard-dijon': ['Dijon mustard', 'mustard-dijon'], 'lemon-extract': ['lemon extract', 'lemon-extract'], 'flour-bread': ['bread flour', 'flour-bread'], 'buttermilk': ['buttermilk', 'buttermilk'], 'pepper-green-chile': ['green chile pepper', 'pepper-green-chile'], 'broccoli': ['broccoli', 'broccoli'], 'ketchup': ['ketchup', 'ketchup'], 'pork-ground': ['ground pork', 'pork-ground'], 'sugar-confectioners': ['confectioners sugaras needed', 'sugar-confectioners'], 'vinegar-balsamic': ['balsamic vinegar', 'vinegar-balsamic'], 'onion-green': ['green onion', 'onion-green'], 'cheese-cream': ['cream cheese', 'cheese-cream'], 'beef-rib-roast-oven-ready': ['oven ready beef rib roast', 'beef-rib-roast-oven-ready'], 'bread-crumbs-dried': ['dried bread crumbs', 'bread-crumbs-dried'], 'tomato-sauce': ['tomato sauce', 'tomato-sauce'], 'oil-vegetable': ['vegetable oil', 'oil-vegetable'], 'brown-veal-stock': ['Brown Veal Stock', 'brown-veal-stock'], 'oil-olive': ['olive oil', 'oil-olive'], 'strawberries': ['strawberries', 'strawberries'], 'tomato-juice': ['tomato juice', 'tomato-juice'], 'wine-dry-white': ['dry white wine', 'wine-dry-white'], 'cheese-cheddar': ['cheddar cheese', 'cheese-cheddar'], 'garlic-powder': ['garlic powder', 'garlic-powder'], 'sugar-granulated': ['granulated sugar', 'sugar-granulated'], 'tomato-paste': ['tomato paste', 'tomato-paste'], 'chili-powder': ['chili powder', 'chili-powder'], 'wine-red': ['red wine', 'wine-red'], 'apple-golden-delicious': ['golden delicious apple', 'apple-golden-delicious'], 'tomatoes-canned': ['canned tomatoes', 'tomatoes-canned'], 'salt-pork': ['salt pork', 'salt-pork'], 'crumb-pie-crust': ['Crumb Pie Crust', 'crumb-pie-crust'], 'brown-stock': ['Brown Stock', 'brown-stock'], 'pecan-halves': ['pecan halves', 'pecan-halves'], 'apple-mcintosh': ['McIntosh apple', 'apple-mcintosh'], 'pecan-pieces': ['pecan pieces', 'pecan-pieces'], 'pepper-ground-black': ['ground black pepper to taste', 'pepper-ground-black'], 'cinnamon-ground': ['ground cinnamon', 'cinnamon-ground'], 'pepper-whole-black': ['whole black pepper', 'pepper-whole-black'], 'fresh-bread-crumbs': ['Fresh Bread Crumbs', 'fresh-bread-crumbs'], 'mushrooms-medium': ['medium mushrooms', 'mushrooms-medium'], 'onion-powder': ['onion powder', 'onion-powder'], 'clarified-butter': ['Clarified Butter', 'clarified-butter'], 'thyme-dried-whole': ['dried whole thyme', 'thyme-dried-whole'], 'vanilla-extract': ['vanilla extract', 'vanilla-extract'], 'salt-kosher': ['kosher salt', 'salt-kosher'], 'yeast-dry-active': ['dry active yeast', 'yeast-dry-active'], 'melon-honeydew': ['honeydew melon', 'melon-honeydew'], 'wine-burgundy': ['Burgundy wine', 'wine-burgundy'], 'egg-whites': ['egg whites', 'egg-whites'], 'milk': ['milk', 'milk'], 'rhubarb-fresh': ['fresh rhubarb', 'rhubarb-fresh'], 'coconut-flaked': ['flaked coconut', 'coconut-flaked'], 'ginger-ground': ['ground ginger', 'ginger-ground'], 'graham-cracker-crumbs': ['graham cracker crumbs', 'graham-cracker-crumbs'], 'pepper-cayenne': ['cayenne pepper', 'pepper-cayenne'], 'pistachio-nuts-shelled': ['shelled pistachio nutsas needed', 'pistachio-nuts-shelled'], 'butter-unsalted': ['unsalted butter', 'butter-unsalted'], 'beef-stock': ['Beef Stock', 'beef-stock'], 'orange-juice': ['orange juice', 'orange-juice'], 'tomatoes-fresh': ['fresh tomatoes', 'tomatoes-fresh'], 'lettuce-bibb': ['bibb lettuce', 'lettuce-bibb'], 'pumpkin-canned': ['canned pumpkin', 'pumpkin-canned'], 'cranberries': ['cranberries', 'cranberries'], 'shortening-vegetable': ['vegetable shortening', 'shortening-vegetable'], 'yeast-instant': ['instant yeast', 'yeast-instant'], 'pastry-cream-cra-me-pa-tissia-re': ['Pastry Cream (Crme Ptissire)as needed', 'pastry-cream-cra-me-pa-tissia-re'], 'salt': ['salt', 'salt'], 'allspice-ground': ['ground allspice', 'allspice-ground'], 'macadamia-nuts-whole': ['whole macadamia nuts', 'macadamia-nuts-whole'], 'lime-zest': ['Lime Zest', 'lime-zest'], 'cloves-whole': ['whole cloves', 'cloves-whole'], 'wine-port': ['port wine', 'wine-port'], 'baking-soda': ['baking soda', 'baking-soda'], 'streusel-topping': ['Streusel Toppingas needed', 'streusel-topping'], 'bacon': ['bacon', 'bacon'], 'wheat-bran': ['wheat bran', 'wheat-bran'], 'eggs': ['eggs', 'eggs'], 'thyme-fresh': ['fresh thyme', 'thyme-fresh'], 'molasses': ['molasses', 'molasses'], 'raisins-dark': ['dark raisins', 'raisins-dark'], 'pepper-ground-white': ['ground white pepper', 'pepper-ground-white'], 'wine-sweet-white': ['sweet white wine', 'wine-sweet-white'], 'egg-yolks-pasteurized': ['pasteurized egg yolks', 'egg-yolks-pasteurized'], 'coconut-shredded': ['shredded coconut', 'coconut-shredded'], 'bay-leaves-dried': ['dried bay leaves', 'bay-leaves-dried'], 'cheese-parmesan': ['parmesan cheese', 'cheese-parmesan'], 'mango': ['mango', 'mango'], 'onion': ['onion', 'onion'], 'corn-syrup-light': ['light corn syrup', 'corn-syrup-light'], 'cream-sour': ['sour cream', 'cream-sour'], 'simple-sourdough-starter': ['Simple Sourdough Starter', 'simple-sourdough-starter'], 'mustard-dry': ['dry mustard', 'mustard-dry'], 'ginger-fresh': ['fresh ginger', 'ginger-fresh'], 'cream-heavy': ['heavy cream', 'cream-heavy'], 'lamb-chops-rib': ['rib lamb chops', 'lamb-chops-rib'], 'espagnole-brown-sauce': ['Espagnole (Brown Sauce)', 'espagnole-brown-sauce'], 'grand-marnier': ['grand marnier', 'grand-marnier'], 'vinegar-cider': ['cider vinegar', 'vinegar-cider'], 'parsley-fresh': ['fresh parsley', 'parsley-fresh'], 'orange-zest': ['Orange Zest', 'orange-zest'], 'yogurt-lowfat': ['lowfat yogurt', 'yogurt-lowfat'], 'wine-white': ['white wine', 'wine-white'], 'water': ['water', 'water'], 'beef-brisket': ['beef brisket', 'beef-brisket'], 'gelatin-powdered': ['powdered gelatin', 'gelatin-powdered'], 'paprika': ['paprika', 'paprika'], 'apple': ['apple', 'apple'], 'apple-granny-smith': ['granny smith apple', 'apple-granny-smith'], 'chicken-velouta': ['Chicken Velout', 'chicken-velouta'], 'milk-evaporated': ['evaporated milk', 'milk-evaporated'], 'bread-sourdough': ['sourdough bread', 'bread-sourdough'], 'vanilla-bean': ['vanilla bean', 'vanilla-bean'], 'beef-ground': ['ground beef', 'beef-ground'], 'marjoram-whole': ['whole marjoram', 'marjoram-whole'], 'beef-brisket-corned': ['corned beef brisket', 'beef-brisket-corned'], 'potato-white': ['white potato', 'potato-white'], 'herb-butter': ['Herb Butter', 'herb-butter'], 'lemon-juice-fresh': ['Lemon Juice (fresh)', 'lemon-juice-fresh'], 'parsnip': ['parsnip', 'parsnip'], 'rhubarb-iqf': ['IQF rhubarb', 'rhubarb-iqf'], 'nutmeg-ground': ['ground nutmeg', 'nutmeg-ground'], 'graham-crackers': ['graham crackers', 'graham-crackers'], 'leeks': ['leeks', 'leeks'], 'blueberries': ['blueberries', 'blueberries'], 'margarine-unsalted': ['unsalted margarine', 'margarine-unsalted'], 'lemon-zest': ['Lemon Zest', 'lemon-zest'], 'butter': ['butter', 'butter'], 'oil-corn': ['corn oil', 'oil-corn'], 'carrot': ['carrot', 'carrot'], 'peaches': ['peaches', 'peaches'], 'mirepoix': ['Mirepoix', 'mirepoix'], 'cumin-ground': ['ground cumin', 'cumin-ground'], 'melon-cantaloupe': ['cantaloupe melon', 'melon-cantaloupe'], 'pineapple': ['pineapple', 'pineapple'], 'food-coloring-red': ['red food coloringas needed', 'food-coloring-red'], 'poppy-seed': ['poppy seed', 'poppy-seed'], 'egg-whites-pasteurized': ['pasteurized egg whites', 'egg-whites-pasteurized'], 'celery': ['celery', 'celery'], 'tomato-pura-e': ['tomato pure', 'tomato-pura-e'], 'cornmeal-yellow': ['yellow cornmealas needed', 'cornmeal-yellow'], 'mealy-pie-dough': ['Mealy Pie Dough', 'mealy-pie-dough'], 'cloves-ground': ['ground cloves', 'cloves-ground'], 'corn-flake-crumbs': ['corn flake crumbs', 'corn-flake-crumbs'], 'garlic': ['garlic', 'garlic'], 'powdered-sugar-glaze': ['Powdered Sugar Glazeas needed', 'powdered-sugar-glaze'], 'honey': ['honey', 'honey'], 'sugar-light-brown': ['light brown sugar', 'sugar-light-brown'], 'vinegar-wine': ['wine vinegar', 'vinegar-wine'], 'anchovy-fillets': ['anchovy fillets', 'anchovy-fillets'], 'flour-cake': ['cake flour', 'flour-cake'], 'flaky-pie-dough': ['Flaky Pie Dough', 'flaky-pie-dough'], 'baking-powder': ['baking powder', 'baking-powder'], 'mushroom-sauce': ['Mushroom Sauceas needed', 'mushroom-sauce'], 'flour-pastry': ['pastry flour', 'flour-pastry']}",
            'reci': '{\'poppy-seed-dressing\': [\'Poppy Seed Dressing\', \'poppy-seed-dressing\'], \'home-style-meatloaf\': [\'Home-Style Meatloaf\', \'home-style-meatloaf\'], \'roasted-corn-chowder\': [\'Roasted Corn Chowder\', \'roasted-corn-chowder\'], \'pumpkin-muffins\': [\'Pumpkin Muffins\', \'pumpkin-muffins\'], \'cinnamon-french-toast\': [\'Cinnamon French Toast\', \'cinnamon-french-toast\'], \'roast-prime-rib-of-beef-au-jus\': [\'Roast Prime Rib of Beef Au Jus\', \'roast-prime-rib-of-beef-au-jus\'], \'applesauce\': [\'Applesauce\', \'applesauce\'], \'sauta-ed-calves-liver-with-onions\': [\'Sauted Calves Liver with Onions\', \'sauta-ed-calves-liver-with-onions\'], \'basic-fudge-frosting\': [\'Basic Fudge Frosting\', \'basic-fudge-frosting\'], \'cream-of-broccoli-soup\': [\'Cream Of Broccoli Soup\', \'cream-of-broccoli-soup\'], \'baked-apples\': [\'Baked Apples\', \'baked-apples\'], \'aunt-ruthie-s-pot-roast\': ["Aunt Ruthie\'s Pot Roast", \'aunt-ruthie-s-pot-roast\'], \'brennan-s-red-wine-and-mushroom-sauce\': ["Brennan\'s Red-Wine and Mushroom Sauce", \'brennan-s-red-wine-and-mushroom-sauce\'], \'coconut-pecan-frosting\': [\'Coconut Pecan Frosting\', \'coconut-pecan-frosting\'], \'grilled-fruit-kebabs\': [\'Grilled Fruit Kebabs\', \'grilled-fruit-kebabs\'], \'cream-cheese-frosting\': [\'Cream Cheese Frosting\', \'cream-cheese-frosting\'], \'lime-chiffon\': [\'Lime Chiffon\', \'lime-chiffon\'], \'crumb-pie-crust\': [\'Crumb Pie Crust\', \'crumb-pie-crust\'], \'english-muffin-loaves\': [\'English Muffin Loaves\', \'english-muffin-loaves\'], \'warm-baked-peaches-or-nectarines\': [\'Warm Baked Peaches or Nectarines\', \'warm-baked-peaches-or-nectarines\'], \'horseradish-cream-sauce\': [\'Horseradish Cream Sauce\', \'horseradish-cream-sauce\'], \'brown-beef-stew\': [\'Brown Beef Stew\', \'brown-beef-stew\'], \'american-pound-cake\': [\'American Pound Cake\', \'american-pound-cake\'], \'caesar-dressing\': [\'Caesar Dressing\', \'caesar-dressing\'], \'flaky-pie-dough-shell\': [\'Flaky Pie Dough Shell\', \'flaky-pie-dough-shell\'], \'cream-of-tomato-soup\': [\'Cream Of Tomato Soup\', \'cream-of-tomato-soup\'], \'cheddar-and-leek-soup\': [\'Cheddar and Leek Soup\', \'cheddar-and-leek-soup\'], \'basic-berry-muffins\': [\'Basic Berry Muffins\', \'basic-berry-muffins\'], \'chili-con-carne\': [\'Chili Con Carne\', \'chili-con-carne\'], \'popovers\': [\'Popovers\', \'popovers\'], \'hugo-s-meatballs\': ["Hugo\'s Meatballs", \'hugo-s-meatballs\'], \'blueberry-muffins\': [\'Blueberry Muffins\', \'blueberry-muffins\'], \'buttermilk-pancakes\': [\'Buttermilk Pancakes\', \'buttermilk-pancakes\'], \'fresh-cranberry-orange-relish\': [\'Fresh Cranberry-Orange Relish\', \'fresh-cranberry-orange-relish\'], \'pecan-sticky-buns\': [\'Pecan Sticky Buns\', \'pecan-sticky-buns\'], \'morning-glory-muffins\': [\'Morning Glory Muffins\', \'morning-glory-muffins\'], \'salisbury-steak\': [\'Salisbury Steak\', \'salisbury-steak\'], \'coconut-macadamia-cake\': [\'Coconut Macadamia Cake\', \'coconut-macadamia-cake\'], \'flaky-pie-dough\': [\'Flaky Pie Dough\', \'flaky-pie-dough\'], \'rhubarb-preserves\': [\'Rhubarb Preserves\', \'rhubarb-preserves\'], \'basic-bran-muffins\': [\'Basic Bran Muffins\', \'basic-bran-muffins\'], \'mealy-pie-dough\': [\'Mealy Pie Dough\', \'mealy-pie-dough\'], \'san-francisco-sourdough-bread\': [\'San Francisco Sourdough Bread\', \'san-francisco-sourdough-bread\'], \'braised-rhubarb\': [\'Braised Rhubarb\', \'braised-rhubarb\'], \'corned-beef-hash\': [\'Corned Beef Hash\', \'corned-beef-hash\'], \'new-york-cheesecake\': [\'New York Cheesecake\', \'new-york-cheesecake\'], \'decorative-cookie-icing\': [\'Decorative Cookie Icing\', \'decorative-cookie-icing\'], \'mealy-pie-dough-shell\': [\'Mealy Pie Dough Shell\', \'mealy-pie-dough-shell\'], \'egg-bacon-lettuce-and-tomato-breakfast-sandwich\': [\'Egg, Bacon, Lettuce and Tomato Breakfast Sandwich\', \'egg-bacon-lettuce-and-tomato-breakfast-sandwich\'], \'brennan-s-lemon-butter-sauce\': ["Brennan\'s Lemon Butter Sauce", \'brennan-s-lemon-butter-sauce\'], \'lemon-poppy-seed-muffins\': [\'Lemon Poppy Seed Muffins\', \'lemon-poppy-seed-muffins\'], \'grilled-lamb-chops-with-herb-butter\': [\'Grilled Lamb Chops with Herb Butter\', \'grilled-lamb-chops-with-herb-butter\'], \'honey-cardamom-butter\': [\'Honey Cardamom Butter\', \'honey-cardamom-butter\'], \'jumbo-cinnamon-buns\': [\'Jumbo Cinnamon Buns\', \'jumbo-cinnamon-buns\'], \'basic-corn-muffins\': [\'Basic Corn Muffins\', \'basic-corn-muffins\'], \'mango-ketchup\': [\'Mango Ketchup\', \'mango-ketchup\'], \'fresh-peach-and-yogurt-soup\': [\'Fresh Peach And Yogurt Soup\', \'fresh-peach-and-yogurt-soup\']}',
            }
        Cuisines.objects.create(**test_dic)
        cuisine_get = Cuisines.objects.get(id=test_dic['id'])
        self.assertEqual(cuisine_get.name, test_dic['name'])
        self.assertEqual(cuisine_get.id_cusine, test_dic['id_cusine'])
        self.assertEqual(cuisine_get.url, test_dic['url'])
        self.assertEqual(cuisine_get.id, test_dic['id'])
        self.assertEqual(cuisine_get.reci, test_dic['reci'])
        self.assertEqual(cuisine_get.ingr, test_dic['ingr'])
        self.assertEqual(cuisine_get.quant_data, test_dic['quant_data'])

    def test_cuisine_model2(self):
        test_dic = {
            'id': 1,
            'id_cusine': 'african',
            'name': 'African',
            'url': '',
            'quant_data': "{'diversity': 0.0, 'diveristy': 0.0, 'popularity': 0.0, 'number_of_recipes': 0, 'number_of_ingredients': 0, 'avg_salt': 0.0}",
            'ingr': '{}',
            'reci': '{}',
            }
        Cuisines.objects.create(**test_dic)
        cuisine_get = Cuisines.objects.get(id=test_dic['id'])
        self.assertEqual(cuisine_get.name, test_dic['name'])
        self.assertEqual(cuisine_get.id_cusine, test_dic['id_cusine'])
        self.assertEqual(cuisine_get.url, test_dic['url'])
        self.assertEqual(cuisine_get.id, test_dic['id'])
        self.assertEqual(cuisine_get.reci, test_dic['reci'])
        self.assertEqual(cuisine_get.ingr, test_dic['ingr'])
        self.assertEqual(cuisine_get.quant_data, test_dic['quant_data'])

    def test_cuisine_model3(self):
        test_dic = {
            'id': 33,
            'id_cusine': 'vietnamese',
            'name': 'Vietnamese',
            'url': '',
            'quant_data': "{'diversity': 1.1570247933884297, 'diveristy': 1.1570247933884297, 'popularity': 0.2, 'number_of_recipes': 1, 'number_of_ingredients': 7, 'avg_salt': 1.095}",
            'ingr': "{'sugar-granulated': ['granulated sugar', 'sugar-granulated'], 'fish-sauce': ['fish sauce', 'fish-sauce'], 'shallot': ['shallot', 'shallot'], 'garlic-clove': ['garlic clove', 'garlic-clove'], 'pepper-thai-chile': ['Thai chile pepper', 'pepper-thai-chile'], 'water': ['water', 'water'], 'lemon-juice-fresh': ['Lemon Juice (fresh)', 'lemon-juice-fresh']}",
            'reci': "{'nuoc-cham-vietnamese-dipping-sauce': ['Nuoc Cham (Vietnamese Dipping Sauce)', 'nuoc-cham-vietnamese-dipping-sauce']}",
            }
        Cuisines.objects.create(**test_dic)
        cuisine_get = Cuisines.objects.get(id=test_dic['id'])
        self.assertEqual(cuisine_get.name, test_dic['name'])
        self.assertEqual(cuisine_get.id_cusine, test_dic['id_cusine'])
        self.assertEqual(cuisine_get.url, test_dic['url'])
        self.assertEqual(cuisine_get.id, test_dic['id'])
        self.assertEqual(cuisine_get.reci, test_dic['reci'])
        self.assertEqual(cuisine_get.ingr, test_dic['ingr'])
        self.assertEqual(cuisine_get.quant_data, test_dic['quant_data'])

    def test_cuisine_model4(self):
        test_dic = {
            'id': 31,
            'id_cusine': 'scandinavian',
            'name': 'Scandinavian',
            'url': '',
            'quant_data': "{'diversity': 1.8181818181818181, 'diveristy': 1.8181818181818181, 'popularity': 0.2, 'number_of_recipes': 1, 'number_of_ingredients': 11, 'avg_salt': 36.61}",
            'ingr': "{'yeast-dry-active': ['dry active yeast', 'yeast-dry-active'], 'butter-unsalted': ['unsalted butter', 'butter-unsalted'], 'sugar-granulated': ['granulated sugar', 'sugar-granulated'], 'cinnamon-ground': ['ground cinnamon', 'cinnamon-ground'], 'eggs': ['eggs', 'eggs'], 'milk': ['milk', 'milk'], 'flour-all-purpose': ['all purpose flour', 'flour-all-purpose'], 'water': ['water', 'water'], 'egg-wash': ['Egg Washas needed', 'egg-wash'], 'vanilla-extract': ['vanilla extract', 'vanilla-extract'], 'salt': ['salt', 'salt']}",
            'reci': "{'danish-pastries': ['Danish Pastries', 'danish-pastries']}",
            }
        Cuisines.objects.create(**test_dic)
        cuisine_get = Cuisines.objects.get(id = test_dic['id'])
        self.assertEqual(cuisine_get.name, test_dic['name'])
        self.assertEqual(cuisine_get.id_cusine, test_dic['id_cusine'])
        self.assertEqual(cuisine_get.url, test_dic['url'])
        self.assertEqual(cuisine_get.id, test_dic['id'])
        self.assertEqual(cuisine_get.reci, test_dic['reci'])
        self.assertEqual(cuisine_get.ingr, test_dic['ingr'])
        self.assertEqual(cuisine_get.quant_data, test_dic['quant_data'])

    def test_cuisine_model5(self):
        test_dic = {
            'id': 24,
            'id_cusine': 'italian',
            'name': 'Italian',
            'url': '',
            'quant_data': "{'diversity': 10.24793388429752, 'diveristy': 10.24793388429752, 'popularity': 3.2, 'number_of_recipes': 16, 'number_of_ingredients': 62, 'avg_salt': 148.5335294117647}",
            'ingr': "{'oregano-fresh': ['fresh oregano', 'oregano-fresh'], 'oil-olive': ['olive oil', 'oil-olive'], 'beef-ground': ['ground beef', 'beef-ground'], 'garlic-clove': ['garlic clove', 'garlic-clove'], 'oil-extra-virgin-olive': ['extra virgin olive oil', 'oil-extra-virgin-olive'], 'mayonnaise': ['mayonnaise', 'mayonnaise'], 'cheese-romano': ['romano cheese', 'cheese-romano'], 'almond-flour': ['almond flour', 'almond-flour'], 'mustard-dijon': ['Dijon mustard', 'mustard-dijon'], 'saffron': ['saffron', 'saffron'], 'wine-dry-white': ['dry white wine', 'wine-dry-white'], 'hazelnuts-whole-unblanched': ['whole unblanched hazelnuts', 'hazelnuts-whole-unblanched'], 'sugar-granulated': ['granulated sugar', 'sugar-granulated'], 'salt': ['salt to taste', 'salt'], 'lime-juice-fresh': ['Lime Juice (fresh)', 'lime-juice-fresh'], 'cheese-mozzarella': ['mozzarella cheese', 'cheese-mozzarella'], 'tomatoes-sun-dried': ['sun-dried tomatoes', 'tomatoes-sun-dried'], 'rosemary-fresh': ['fresh rosemary', 'rosemary-fresh'], 'cheese-provolone': ['provolone cheese', 'cheese-provolone'], 'chicken-stock': ['Chicken Stock', 'chicken-stock'], 'flour-pastry': ['pastry flour', 'flour-pastry'], 'nutmeg-ground': ['ground nutmeg to taste', 'nutmeg-ground'], 'flour-all-purpose': ['all purpose flouras needed', 'flour-all-purpose'], 'pepper-ground-black': ['ground black pepper to taste', 'pepper-ground-black'], 'chocolate-semisweet': ['semisweet chocolateas needed', 'chocolate-semisweet'], 'eggs': ['eggs', 'eggs'], 'barley': ['barley', 'barley'], 'butter': ['butter', 'butter'], 'carrot': ['carrot', 'carrot'], 'capers': ['capers', 'capers'], 'mirepoix': ['Mirepoix', 'mirepoix'], 'white-stock': ['White Stock', 'white-stock'], 'pine-nuts': ['pine nuts', 'pine-nuts'], 'cheese-parmesan': ['parmesan cheese', 'cheese-parmesan'], 'eggplant-japanese': ['Japanese eggplant', 'eggplant-japanese'], 'onion': ['onion', 'onion'], 'corn-syrup-light': ['light corn syrup', 'corn-syrup-light'], 'thyme-fresh': ['fresh thyme', 'thyme-fresh'], 'yeast-dry-active': ['dry active yeast', 'yeast-dry-active'], 'flour-bread': ['bread flour', 'flour-bread'], 'rice-arborio': ['arborio rice', 'rice-arborio'], 'oil-soybean': ['soybean oil', 'oil-soybean'], 'basil-fresh': ['fresh basil', 'basil-fresh'], 'panko': ['panko', 'panko'], 'milk': ['milk', 'milk'], 'salt-kosher': ['kosher salt to taste', 'salt-kosher'], 'tomato-concassa': ['Tomato Concass', 'tomato-concassa'], 'hazelnut-flour': ['hazelnut flour', 'hazelnut-flour'], 'pizza-dough': ['Pizza Dough', 'pizza-dough'], 'onion-green': ['green onion', 'onion-green'], 'basic-pasta-dough': ['Basic Pasta Dough', 'basic-pasta-dough'], 'garlic': ['garlic', 'garlic'], 'cheese-asiago': ['asiago cheese', 'cheese-asiago'], 'beef-tenderloin': ['beef tenderloin', 'beef-tenderloin'], 'butter-unsalted': ['unsalted butter', 'butter-unsalted'], 'cinnamon-ground': ['ground cinnamon', 'cinnamon-ground'], 'wine-white': ['white wine', 'wine-white'], 'egg-whites': ['egg whites', 'egg-whites'], 'baking-powder': ['baking powder', 'baking-powder'], 'water': ['water', 'water'], 'spinach-fresh': ['fresh spinach', 'spinach-fresh'], 'pepper-cracked-black': ['cracked black pepper to taste', 'pepper-cracked-black']}",
            'reci': "{'biscotti': ['Biscotti', 'biscotti'], 'fresh-spinach-pasta-dough': ['Fresh Spinach Pasta Dough', 'fresh-spinach-pasta-dough'], 'ricotta-cheese': ['Ricotta Cheese', 'ricotta-cheese'], 'risotto-milanese': ['Risotto Milanese', 'risotto-milanese'], 'fresh-pasta-sheets': ['Fresh Pasta Sheets', 'fresh-pasta-sheets'], 'basic-pasta-dough': ['Basic Pasta Dough', 'basic-pasta-dough'], 'risotto-cakes': ['Risotto Cakes', 'risotto-cakes'], 'pesto-sauce': ['Pesto Sauce', 'pesto-sauce'], 'fresh-tomato-sauce-for-pasta': ['Fresh Tomato Sauce for Pasta', 'fresh-tomato-sauce-for-pasta'], 'focaccia-roman-flatbread': ['Focaccia (Roman Flatbread)', 'focaccia-roman-flatbread'], 'carpaccio': ['Carpaccio', 'carpaccio'], 'chocolate-italian-buttercream': ['Chocolate Italian Buttercream', 'chocolate-italian-buttercream'], 'eggplant-and-sun-dried-tomato-pizza': ['Eggplant and Sun-Dried Tomato Pizza', 'eggplant-and-sun-dried-tomato-pizza'], 'bolognese-sauce': ['Bolognese Sauce', 'bolognese-sauce'], 'italian-meringue': ['Italian Meringue', 'italian-meringue'], 'barley-risotto': ['Barley Risotto', 'barley-risotto']}",
            }
        Cuisines.objects.create(**test_dic)
        cuisine_get = Cuisines.objects.get(id = test_dic['id'])
        self.assertEqual(cuisine_get.name, test_dic['name'])
        self.assertEqual(cuisine_get.id_cusine, test_dic['id_cusine'])
        self.assertEqual(cuisine_get.url, test_dic['url'])
        self.assertEqual(cuisine_get.id, test_dic['id'])
        self.assertEqual(cuisine_get.reci, test_dic['reci'])
        self.assertEqual(cuisine_get.ingr, test_dic['ingr'])
        self.assertEqual(cuisine_get.quant_data, test_dic['quant_data'])

    def test_ingredients_model1(self):
        test_dict = {
            'id': 1,
            'ing_id': 'water',
            'name': 'water',
            'quant_data': "{'diveristy': 39.39393939393939, 'number_of_recipes': 94, 'popularity': 18.8, 'calories_per_100g': 0.0, 'number_of_cuisines': 13}",
            'nut_info': "{'protein': '0.0 g per 100g ', 'carbohydrates': '0.0 g per 100g ', 'saturated fat': '0.0 g per 100g ', 'fat': '0.0 g per 100g ', 'iron': '0.0 mg per 100g ', 'calories from fat': '0.0 kcal per 100g ', 'trans fat': '0.0 g per 100g ', 'cholesterol': '0.0 mg per 100g ', 'calories': '0.0 kcal per 100g ', 'vitamin a': '0.0 IU per 100g ', 'vitamin c': '0.0 mg per 100g ', 'calcium': '3.0 mg per 100g ', 'sodium': '4.0 mg per 100g '}",
            'all_cuisines': "{'n-a': ['N/A', 'n-a'], 'american-mountain-states': ['American: Mountain States', 'american-mountain-states'], 'american': ['American', 'american'], 'scandinavian': ['Scandinavian', 'scandinavian'], 'mexican': ['Mexican', 'mexican'], 'american-the-melting-pot': ['American: The Melting Pot', 'american-the-melting-pot'], 'asian': ['Asian', 'asian'], 'american-new-england': ['American: New England', 'american-new-england'], 'italian': ['Italian', 'italian'], 'indian': ['Indian', 'indian'], 'american-southwest': ['American: Southwest', 'american-southwest'], 'french': ['French', 'french'], 'vietnamese': ['Vietnamese', 'vietnamese']}",
            'all_recipes': "{'risotto-cakes': ['Risotto Cakes', 'risotto-cakes'], 'caramelized-berry-sauce': ['Caramelized Berry Sauce', 'caramelized-berry-sauce'], 'sugar-syrup-medium': ['Sugar Syrup (medium)', 'sugar-syrup-medium'], 'focaccia-roman-flatbread': ['Focaccia (Roman Flatbread)', 'focaccia-roman-flatbread'], 'lamb-jus-lia': ['Lamb Jus Li', 'lamb-jus-lia'], 'chicken-stock': ['Chicken Stock', 'chicken-stock'], 'white-chocolate-buttercream': ['White Chocolate Buttercream', 'white-chocolate-buttercream'], 'white-chicken-stock': ['White Chicken Stock', 'white-chicken-stock'], 'shallot-curry-oil': ['Shallot Curry Oil', 'shallot-curry-oil'], 'crunchy-granola': ['Crunchy Granola', 'crunchy-granola'], 'shellfish-stock': ['Shellfish Stock', 'shellfish-stock'], 'cream-of-tomato-soup': ['Cream Of Tomato Soup', 'cream-of-tomato-soup'], 'brown-stock': ['Brown Stock', 'brown-stock'], 'creole-ra-moulade': ['Creole Rmoulade', 'creole-ra-moulade'], 'watermelon-and-cherry-salad-with-fresh-mint-syrup': ['Watermelon and Cherry Salad with Fresh Mint Syrup', 'watermelon-and-cherry-salad-with-fresh-mint-syrup'], 'curried-chickpea-crisps': ['Curried Chickpea Crisps', 'curried-chickpea-crisps'], 'veal-stock': ['Veal Stock', 'veal-stock'], 'fish-fumet': ['Fish Fumet', 'fish-fumet'], 'danish-pastries': ['Danish Pastries', 'danish-pastries'], 'rabbit-stock': ['Rabbit Stock', 'rabbit-stock'], 'simple-syrup': ['Simple Syrup', 'simple-syrup'], 'soy-dipping-sauce': ['Soy Dipping Sauce', 'soy-dipping-sauce'], 'french-or-italian-bread': ['French or Italian Bread', 'french-or-italian-bread'], 'shrimp-stock': ['Shrimp Stock', 'shrimp-stock'], 'black-bean-spread': ['Black Bean Spread', 'black-bean-spread'], 'minted-cheese-mousse': ['Minted Cheese Mousse', 'minted-cheese-mousse'], 'redfish-sopa-base': ['Redfish Sopa Base', 'redfish-sopa-base'], 'court-bouillon': ['Court Bouillon', 'court-bouillon'], 'beef-stock': ['Beef Stock', 'beef-stock'], 'candied-citrus-rind': ['Candied Citrus Rind', 'candied-citrus-rind'], 'diplomat-cream-filling': ['Diplomat Cream Filling', 'diplomat-cream-filling'], 'apple-salsa': ['Apple Salsa', 'apple-salsa'], 'beet-vinaigrette': ['Beet Vinaigrette', 'beet-vinaigrette'], 'savory-crepes': ['Savory Crepes', 'savory-crepes'], 'new-england-style-clam-chowder': ['New England-Style Clam Chowder', 'new-england-style-clam-chowder'], 'tomatillo-salsa': ['Tomatillo Salsa', 'tomatillo-salsa'], 'rhubarb-preserves': ['Rhubarb Preserves', 'rhubarb-preserves'], 'lobster-stock': ['Lobster Stock', 'lobster-stock'], 'passion-fruit-cra-me-chiboust': ['Passion Fruit Crme Chiboust', 'passion-fruit-cra-me-chiboust'], 'simmered-rice': ['Simmered Rice', 'simmered-rice'], 'mustard-vinaigrette-dressing': ['Mustard Vinaigrette Dressing', 'mustard-vinaigrette-dressing'], 'caramel-sauce': ['Caramel Sauce', 'caramel-sauce'], 'hollandaise': ['Hollandaise', 'hollandaise'], 'brown-veal-stock': ['Brown Veal Stock', 'brown-veal-stock'], 'orange-gastrique': ['Orange Gastrique', 'orange-gastrique'], 'barley-risotto': ['Barley Risotto', 'barley-risotto'], 'lime-chiffon': ['Lime Chiffon', 'lime-chiffon'], 'soft-yeast-dinner-rolls': ['Soft Yeast Dinner Rolls', 'soft-yeast-dinner-rolls'], 'white-stock': ['White Stock', 'white-stock'], 'pizza-dough': ['Pizza Dough', 'pizza-dough'], 'dark-chocolate-syrup': ['Dark Chocolate Syrup', 'dark-chocolate-syrup'], 'turtle-cheesecake': ['Turtle Cheesecake', 'turtle-cheesecake'], 'whole-wheat-bread': ['Whole-Wheat Bread', 'whole-wheat-bread'], 'fresh-cranberry-orange-relish': ['Fresh Cranberry-Orange Relish', 'fresh-cranberry-orange-relish'], 'puff-pastry': ['Puff Pastry', 'puff-pastry'], 'breadsticks': ['Breadsticks', 'breadsticks'], 'english-muffin-loaves': ['English Muffin Loaves', 'english-muffin-loaves'], 'duck-stock': ['Duck Stock', 'duck-stock'], 'risotto-milanese': ['Risotto Milanese', 'risotto-milanese'], 'nuoc-cham-vietnamese-dipping-sauce': ['Nuoc Cham (Vietnamese Dipping Sauce)', 'nuoc-cham-vietnamese-dipping-sauce'], 'dough-for-pa-ta': ['Dough for Pt', 'dough-for-pa-ta'], 'fish-stock': ['Fish Stock', 'fish-stock'], 'smoked-bacon-and-black-quinoa-pilaf': ['Smoked Bacon and Black Quinoa Pilaf', 'smoked-bacon-and-black-quinoa-pilaf'], 'poached-eggs': ['Poached Eggs', 'poached-eggs'], 'pork-stock': ['Pork Stock', 'pork-stock'], 'mushroom-sauce': ['Mushroom Sauce', 'mushroom-sauce'], 'powdered-sugar-glaze': ['Powdered Sugar Glaze', 'powdered-sugar-glaze'], 'toffee-caramel-flan': ['Toffee Caramel Flan', 'toffee-caramel-flan'], 'vegetable-stock': ['Vegetable Stock', 'vegetable-stock'], 'brioche-dough': ['Brioche Dough', 'brioche-dough'], 'pinto-beans': ['Pinto Beans', 'pinto-beans'], 'white-veal-stock': ['White Veal Stock', 'white-veal-stock'], 'basic-fudge-frosting': ['Basic Fudge Frosting', 'basic-fudge-frosting'], 'cooked-long-grain-rice': ['Cooked Long-Grain Rice', 'cooked-long-grain-rice'], 'game-stock': ['Game Stock', 'game-stock'], 'brioche': ['Brioche', 'brioche'], 'white-sandwich-bread': ['White Sandwich Bread', 'white-sandwich-bread'], 'jus-lia': ['Jus Li', 'jus-lia'], 'san-francisco-sourdough-bread': ['San Francisco Sourdough Bread', 'san-francisco-sourdough-bread'], 'naan-indian-flatbread': ['Naan (Indian Flatbread)', 'naan-indian-flatbread'], 'gingered-dal': ['Gingered Dal', 'gingered-dal'], 'cra-me-chiboust': ['Crme Chiboust', 'cra-me-chiboust'], 'pho-bo-hanoi-beef-and-noodle-soup': ['Pho Bo (Hanoi Beef and Noodle Soup)', 'pho-bo-hanoi-beef-and-noodle-soup'], 'harvest-lobster-and-corn-chowder': ['Harvest Lobster and Corn Chowder', 'harvest-lobster-and-corn-chowder'], 'lamb-stock': ['Lamb Stock', 'lamb-stock'], 'chocolate-italian-buttercream': ['Chocolate Italian Buttercream', 'chocolate-italian-buttercream'], 'dried-fruit-compote': ['Dried Fruit Compote', 'dried-fruit-compote'], 'light-rye-bread': ['Light Rye Bread', 'light-rye-bread'], 'pheasant-stock': ['Pheasant Stock', 'pheasant-stock'], 'matzo-balls': ['Matzo Balls', 'matzo-balls'], 'italian-meringue': ['Italian Meringue', 'italian-meringue'], 'cra-pes': ['Crpes', 'cra-pes'], 'challah': ['Challah', 'challah'], 'peanut-sauce': ['Peanut Sauce', 'peanut-sauce']}",
            }
        Ingredients.objects.create(**test_dict)
        ingredients_get = Ingredients.objects.get(id=test_dict['id'])
        self.assertEqual(ingredients_get.ing_id, test_dict['ing_id'])
        self.assertEqual(ingredients_get.name, test_dict['name'])
        self.assertEqual(ingredients_get.quant_data,
                         test_dict['quant_data'])
        self.assertEqual(ingredients_get.nut_info, test_dict['nut_info'
                         ])
        self.assertEqual(ingredients_get.all_cuisines,
                         test_dict['all_cuisines'])
        self.assertEqual(ingredients_get.all_recipes,
                         test_dict['all_recipes'])

    def test_ingredients_model2(self):
        test_dict = {
            'id': 100,
            'ing_id': 'frangelico',
            'name': 'frangelico',
            'quant_data': "{'diveristy': 3.0303030303030303, 'number_of_recipes': 1, 'popularity': 0.2, 'calories_per_100g': 0.0, 'number_of_cuisines': 1}",
            'nut_info': '{}',
            'all_cuisines': "{'french': ['French', 'french']}",
            'all_recipes': "{'frangelico-custard-sauce': ['Frangelico Custard Sauce', 'frangelico-custard-sauce']}",
            }
        Ingredients.objects.create(**test_dict)
        ingredients_get = Ingredients.objects.get(id=test_dict['id'])
        self.assertEqual(ingredients_get.ing_id, test_dict['ing_id'])
        self.assertEqual(ingredients_get.name, test_dict['name'])
        self.assertEqual(ingredients_get.quant_data,
                         test_dict['quant_data'])
        self.assertEqual(ingredients_get.nut_info, test_dict['nut_info'
                         ])
        self.assertEqual(ingredients_get.all_cuisines,
                         test_dict['all_cuisines'])
        self.assertEqual(ingredients_get.all_recipes,
                         test_dict['all_recipes'])

    def test_ingredients_model3(self):
        test_dict = {
            'id': 200,
            'ing_id': 'butter',
            'name': 'butter',
            'quant_data': "{'diveristy': 30.303030303030305, 'number_of_recipes': 83, 'popularity': 16.6, 'calories_per_100g': 717.0, 'number_of_cuisines': 10}",
            'nut_info': "{'protein': '0.85 g per 100g ', 'carbohydrates': '0.06 g per 100g ', 'saturated fat': '51.368 g per 100g ', 'fat': '81.11 g per 100g ', 'iron': '0.02 mg per 100g ', 'calories from fat': '729.99 kcal per 100g ', 'trans fat': '0.0 g per 100g ', 'cholesterol': '215.0 mg per 100g ', 'calories': '717.0 kcal per 100g ', 'vitamin a': '2499.0 IU per 100g ', 'vitamin c': '0.0 mg per 100g ', 'calcium': '24.0 mg per 100g ', 'sodium': '11.0 mg per 100g '}",
            'all_cuisines': "{'austrian': ['Austrian', 'austrian'], 'n-a': ['N/A', 'n-a'], 'american': ['American', 'american'], 'italian': ['Italian', 'italian'], 'american-southern': ['American: Southern', 'american-southern'], 'british-isles': ['British Isles', 'british-isles'], 'french': ['French', 'french'], 'indian': ['Indian', 'indian'], 'russian-eastern-european': ['Russian / Eastern European', 'russian-eastern-european'], 'american-new-england': ['American: New England', 'american-new-england']}",
            'all_recipes': '{\'savory-fruit-compote\': [\'Savory Fruit Compote\', \'savory-fruit-compote\'], \'new-york-cheesecake\': [\'New York Cheesecake\', \'new-york-cheesecake\'], \'orange-gastrique\': [\'Orange Gastrique\', \'orange-gastrique\'], \'barley-risotto\': [\'Barley Risotto\', \'barley-risotto\'], \'breaded-veal-cutlets\': [\'Breaded Veal Cutlets\', \'breaded-veal-cutlets\'], \'cherry-confit\': [\'Cherry Confit\', \'cherry-confit\'], \'soubise-sauce\': [\'Soubise Sauce\', \'soubise-sauce\'], \'beurre-rouge\': [\'Beurre Rouge\', \'beurre-rouge\'], \'cheese-blintzes\': [\'Cheese Blintzes\', \'cheese-blintzes\'], \'beurre-mania\': [\'Beurre Mani\', \'beurre-mania\'], \'velouta\': [\'Velout\', \'velouta\'], \'phyllo-crisps\': [\'Phyllo Crisps\', \'phyllo-crisps\'], \'sorrel-sauce\': [\'Sorrel Sauce\', \'sorrel-sauce\'], \'mashed-potatoes\': [\'Mashed Potatoes\', \'mashed-potatoes\'], \'cream-of-tomato-soup\': [\'Cream Of Tomato Soup\', \'cream-of-tomato-soup\'], \'whole-wheat-bread\': [\'Whole-Wheat Bread\', \'whole-wheat-bread\'], \'garlic-croutons\': [\'Garlic Croutons\', \'garlic-croutons\'], \'goat-cheese-and-potato-custard\': [\'Goat Cheese and Potato Custard\', \'goat-cheese-and-potato-custard\'], \'streusel-topping\': [\'Streusel Topping\', \'streusel-topping\'], \'milanaise-sauce\': [\'Milanaise Sauce\', \'milanaise-sauce\'], \'shortcakes\': [\'Shortcakes\', \'shortcakes\'], \'brennan-s-red-wine-and-mushroom-sauce\': ["Brennan\'s Red-Wine and Mushroom Sauce", \'brennan-s-red-wine-and-mushroom-sauce\'], \'spiced-pecans\': [\'Spiced Pecans\', \'spiced-pecans\'], \'fish-velouta\': [\'Fish Velout\', \'fish-velouta\'], \'chocolate-souffla-s\': [\'Chocolate Souffls\', \'chocolate-souffla-s\'], \'risotto-milanese\': [\'Risotto Milanese\', \'risotto-milanese\'], \'hungarian-sauce\': [\'Hungarian Sauce\', \'hungarian-sauce\'], \'vichyssoise-cold-potato-leek-soup\': [\'Vichyssoise (Cold Potato-Leek Soup)\', \'vichyssoise-cold-potato-leek-soup\'], \'thyme-scented-celery-essence\': [\'Thyme-Scented Celery Essence\', \'thyme-scented-celery-essence\'], \'duchesse-potatoes\': [\'Duchesse Potatoes\', \'duchesse-potatoes\'], \'horseradish-cream-sauce\': [\'Horseradish Cream Sauce\', \'horseradish-cream-sauce\'], \'mint-and-celeriac-sauce\': [\'Mint and Celeriac Sauce\', \'mint-and-celeriac-sauce\'], \'aurora-sauce\': [\'Aurora Sauce\', \'aurora-sauce\'], \'tulipe-cookies\': [\'Tulipe Cookies\', \'tulipe-cookies\'], \'fish-fumet\': [\'Fish Fumet\', \'fish-fumet\'], \'parsnip-pura-e\': [\'Parsnip Pure\', \'parsnip-pura-e\'], \'tomato-butter-sauce-with-thyme\': [\'Tomato Butter Sauce with Thyme\', \'tomato-butter-sauce-with-thyme\'], \'bolognese-sauce\': [\'Bolognese Sauce\', \'bolognese-sauce\'], \'garlic-tuiles\': [\'Garlic Tuiles\', \'garlic-tuiles\'], \'poulette-sauce\': [\'Poulette Sauce\', \'poulette-sauce\'], \'veal-velouta\': [\'Veal Velout\', \'veal-velouta\'], \'entreca-tes-bordelaise\': [\'Entrectes Bordelaise\', \'entreca-tes-bordelaise\'], \'mushroom-sauce\': [\'Mushroom Sauce\', \'mushroom-sauce\'], \'strawberry-cra-pes-fitzgerald\': [\'Strawberry Crpes Fitzgerald\', \'strawberry-cra-pes-fitzgerald\'], \'beurre-blanc\': [\'Beurre Blanc\', \'beurre-blanc\'], \'persillade\': [\'Persillade\', \'persillade\'], \'chasseur-hunter-s-sauce\': ["Chasseur (Hunter\'s Sauce)", \'chasseur-hunter-s-sauce\'], \'mornay-sauce\': [\'Mornay Sauce\', \'mornay-sauce\'], \'minute-steak-dijonaise\': [\'Minute Steak Dijonaise\', \'minute-steak-dijonaise\'], \'carrot-pura-e\': [\'Carrot Pure\', \'carrot-pura-e\'], \'chevreuil-sauce\': [\'Chevreuil Sauce\', \'chevreuil-sauce\'], \'shirred-eggs-with-ham\': [\'Shirred Eggs with Ham\', \'shirred-eggs-with-ham\'], \'blond-roux\': [\'Blond Roux\', \'blond-roux\'], \'chocolate-italian-buttercream\': [\'Chocolate Italian Buttercream\', \'chocolate-italian-buttercream\'], \'rolled-souffla\': [\'Rolled Souffl\', \'rolled-souffla\'], \'clarified-butter\': [\'Clarified Butter\', \'clarified-butter\'], \'cheddar-and-leek-soup\': [\'Cheddar and Leek Soup\', \'cheddar-and-leek-soup\'], \'honey-cardamom-butter\': [\'Honey Cardamom Butter\', \'honey-cardamom-butter\'], \'robert-sauce\': [\'Robert Sauce\', \'robert-sauce\'], \'smoked-corn-pudding\': [\'Smoked Corn Pudding\', \'smoked-corn-pudding\'], \'new-england-style-clam-chowder\': [\'New England-Style Clam Chowder\', \'new-england-style-clam-chowder\'], \'brennan-s-lemon-butter-sauce\': ["Brennan\'s Lemon Butter Sauce", \'brennan-s-lemon-butter-sauce\'], \'filet-of-beef-with-coffee-beans\': [\'Filet of Beef with Coffee Beans\', \'filet-of-beef-with-coffee-beans\'], \'crumb-pie-crust\': [\'Crumb Pie Crust\', \'crumb-pie-crust\'], \'veal-marsala\': [\'Veal Marsala\', \'veal-marsala\'], \'lobster-stock\': [\'Lobster Stock\', \'lobster-stock\'], \'gingered-dal\': [\'Gingered Dal\', \'gingered-dal\'], \'white-roux\': [\'White Roux\', \'white-roux\'], \'potato-and-celeriac-pura-e\': [\'Potato and Celeriac Pure\', \'potato-and-celeriac-pura-e\'], \'harvest-lobster-and-corn-chowder\': [\'Harvest Lobster and Corn Chowder\', \'harvest-lobster-and-corn-chowder\'], \'cha-teaubriand-sauce\': [\'Chteaubriand Sauce\', \'cha-teaubriand-sauce\'], \'boeuf-a-la-ficelle-beef-poached-on-a-string\': [\'Boeuf \\xa0 la Ficelle (Beef Poached on a String)\', \'boeuf-a-la-ficelle-beef-poached-on-a-string\'], \'ra-sti-potatoes\': [\'Rsti Potatoes\', \'ra-sti-potatoes\'], \'bordelaise-sauce\': [\'Bordelaise Sauce\', \'bordelaise-sauce\'], \'popovers\': [\'Popovers\', \'popovers\'], \'hearty-vegetable-beef-soup\': [\'Hearty Vegetable Beef Soup\', \'hearty-vegetable-beef-soup\'], \'bercy-sauce\': [\'Bercy Sauce\', \'bercy-sauce\'], \'cream-of-broccoli-soup\': [\'Cream Of Broccoli Soup\', \'cream-of-broccoli-soup\'], \'togarishi-yams\': [\'Togarishi Yams\', \'togarishi-yams\'], \'duxelles\': [\'Duxelles\', \'duxelles\'], \'sweetbreads-grenoble\': [\'Sweetbreads Grenoble\', \'sweetbreads-grenoble\'], \'poivrade-sauce\': [\'Poivrade Sauce\', \'poivrade-sauce\'], \'roux\': [\'Roux\', \'roux\']}',
            }
        Ingredients.objects.create(**test_dict)
        ingredients_get = Ingredients.objects.get(id=test_dict['id'])
        self.assertEqual(ingredients_get.ing_id, test_dict['ing_id'])
        self.assertEqual(ingredients_get.name, test_dict['name'])
        self.assertEqual(ingredients_get.quant_data,
                         test_dict['quant_data'])
        self.assertEqual(ingredients_get.nut_info, test_dict['nut_info'
                         ])
        self.assertEqual(ingredients_get.all_cuisines,
                         test_dict['all_cuisines'])
        self.assertEqual(ingredients_get.all_recipes,
                         test_dict['all_recipes'])

    def test_ingredients_model4(self):
        test_dict = {
            'id': 300,
            'ing_id': 'turkey-breast-4-7-lb-bone-in',
            'name': 'bone in turkey breast 4-7 lb',
            'quant_data': "{'diveristy': 3.0303030303030303, 'number_of_recipes': 1, 'popularity': 0.2, 'calories_per_100g': 0.0, 'number_of_cuisines': 1}",
            'nut_info': '{}',
            'all_cuisines': "{'n-a': ['N/A', 'n-a']}",
            'all_recipes': "{'turkey-breast-scallops-3-oz': ['Turkey Breast Scallops (3 oz)', 'turkey-breast-scallops-3-oz']}",
            }
        Ingredients.objects.create(**test_dict)
        ingredients_get = Ingredients.objects.get(id=test_dict['id'])
        self.assertEqual(ingredients_get.ing_id, test_dict['ing_id'])
        self.assertEqual(ingredients_get.name, test_dict['name'])
        self.assertEqual(ingredients_get.quant_data,
                         test_dict['quant_data'])
        self.assertEqual(ingredients_get.nut_info, test_dict['nut_info'
                         ])
        self.assertEqual(ingredients_get.all_cuisines,
                         test_dict['all_cuisines'])
        self.assertEqual(ingredients_get.all_recipes,
                         test_dict['all_recipes'])

    def test_ingredients_model5(self):
        test_dict = {
            'id': 427,
            'ing_id': 'vinegar-champagne',
            'name': 'Champagne vinegar',
            'quant_data': "{'diveristy': 3.0303030303030303, 'number_of_recipes': 1, 'popularity': 0.2, 'calories_per_100g': 0.0, 'number_of_cuisines': 1}",
            'nut_info': '{}',
            'all_cuisines': "{'french': ['French', 'french']}",
            'all_recipes': "{'tarragon-aa-oli': ['Tarragon Aoli', 'tarragon-aa-oli']}",
            }
        Ingredients.objects.create(**test_dict)
        ingredients_get = Ingredients.objects.get(id=test_dict['id'])
        self.assertEqual(ingredients_get.ing_id, test_dict['ing_id'])
        self.assertEqual(ingredients_get.name, test_dict['name'])
        self.assertEqual(ingredients_get.quant_data,
                         test_dict['quant_data'])
        self.assertEqual(ingredients_get.nut_info, test_dict['nut_info'
                         ])
        self.assertEqual(ingredients_get.all_cuisines,
                         test_dict['all_cuisines'])
        self.assertEqual(ingredients_get.all_recipes,
                         test_dict['all_recipes'])

