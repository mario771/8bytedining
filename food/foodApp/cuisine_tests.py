
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
   def test_cuisine_model2(self):
      test_dic =  {
      "id": 1,
      "id_cusine": "african",
      "name": "African",
      "url": "",
      "quant_data": "{'diversity': 0.0, 'diveristy': 0.0, 'popularity': 0.0, 'number_of_recipes': 0, 'number_of_ingredients': 0, 'avg_salt': 0.0}",
      "ingr": "{}",
      "reci": "{}"}
      Cuisines.objects.create(**test_dic)
      cuisine_get = Cuisines.objects.get(id = test_dic["id"])
      self.assertEqual(cuisine_get.name, test_dic["name"])
      self.assertEqual(cuisine_get.id_cusine,test_dic["id_cusine"])
      self.assertEqual(cuisine_get.url,test_dic["url"])
      self.assertEqual(cuisine_get.id,test_dic["id"])
      self.assertEqual(cuisine_get.reci, test_dic["reci"])
      self.assertEqual(cuisine_get.ingr, test_dic["ingr"])
      self.assertEqual(cuisine_get.quant_data, test_dic["quant_data"] )
