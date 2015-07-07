from django.db import models

# Create your models here.

#-------------
#Recipe Model
#-------------

class Recipes(models.Model) : 

 """ 
  The Recipe model returns name, id (recipe name)  url,
  cusine, cooking method, ingredients, image, and thumb
 """

 name = models.CharField(max_length=500)
 recipe_id = models.CharField(max_length=500)
 url = models.CharField(max_length=500)
 cusine = models.CharField(max_length=500)
 cooking_method = models.CharField(max_length = 500)
 # How to put ingredients into list?? I think there's models.ManytoMany ?
 image = models.CharField(max_length=500) 
 thumb = models.CharField(max_length =500)

 def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/Recipes/%s/" % url_name

 def __str__ (self):
        return self.full_name
  
#------------------
#Ingredients Model
#------------------

class Ingredients(models.Model) :

   """
   
   """
   
  
   def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/ingredients/%s/" % url_name

   def __str__ (self):
        return self.full_name

#------------
#Cusine Model
#------------

class Cusine (models.Model) :

   """
   Cusine contains a name, an id (name), url, and recipe count
   """

   name = models.CharField(max_length=500)
   cusine_id = models.CharField(max_length=500)
   url = models.CharField(max_length=500)
   recipe_count = models.IntegerField(default=0)

   def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/cusine/%s/" % url_name

   def __str__ (self):
        return self.full_name

