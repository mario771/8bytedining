from django.db import models

# Create your models here.

#-------------
#Recipe Model
#-------------

#class Recipes (models.Model) : 
#
# """ 
#  The Recipe model returns name, id (recipe name)  url,
#  cuisine, cooking method, ingredients, and image
# """

# name = models.CharField(max_length=500)
# recipe_id = models.CharField(max_length=500)
# url = models.CharField(max_length=500)
# directions = models.CharField(max_length= 5000, default = "")
# nutritionalInfo = models.CharField(max_length=5000, default = "")
# cuisineGivenRecipe = models.CharField(max_length=500)
# ingredients = models.ForeignKey("Ingredients", default = "")
# # How to put ingredients into list?? I think there's models.ManytoMany ?
# image = models.CharField(max_length=500)
#
# def get_absolute_url(self):
#        url_name = self.full_name.replace(' ', '_')
#        return "/Recipes/%s/" % url_name
#
# def __str__ (self):
#        return self.full_name
#  
##------------------
##Ingredients Model
##------------------
#
#class Ingredients (models.Model) :
#
#   name = models.CharField(max_length=500, default="")
#   recipe_count = models.IntegerField(default=0)
#
#   
#  
#   def get_absolute_url(self):
#        url_name = self.full_name.replace(' ', '_')
#        return "/ingredients/%s/" % url_name
#
#   def __str__ (self):
#        return self.full_name
#
##------------
##Cuisine Model
##------------
#
#class Cuisine(models.Model) :
#
#   """
#   Cuisine contains a name, an id (name), url, and recipe count
#   """
#
#   name = models.CharField(max_length=500)
#   cuisine_id = models.CharField(max_length=500)
#   url = models.CharField(max_length=500)
#   recipe_count = models.IntegerField(default=0)
#   ingredients = models.ForeignKey('Ingredients', default = "")
#   recipes = models.ForeignKey("Recipes", default = "")
#   def get_absolute_url(self):
#        url_name = self.full_name.replace(' ', '_')
#        return "/cuisine/%s/" % url_name
#
#   def __str__ (self):
#        return self.full_name

class Thing(models.Model) :
   name = models.CharField(max_length=20)
   number = models.IntegerField(default=0)

