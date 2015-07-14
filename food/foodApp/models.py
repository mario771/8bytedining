from django.db import models

# Create your models here.

#------------------
#Ingredients Model
#------------------

class Ingredients (models.Model) :
   ing_id = models.CharField(max_length=500, default="") 
   name = models.CharField(max_length=500, default="")
   recipe_count = models.IntegerField(default=0)
   quant_data = models.CharField(max_length=500, default="")
   nut_info = models.CharField(max_length=5000)
  
   def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/ingredients/%s/" % url_name

   def __str__ (self):
        return self.full_name
#------------
#Cuisines Model
#------------

class Cuisines(models.Model) :

   """
   Cuisines contains a name, an id (name), url, and recipe count
   """
   cuisine = models.CharField(max_length=500)
   name = models.CharField(max_length=500)
   url = models.CharField(max_length=500)
   recipe_count = models.IntegerField(default=0)
   quant_data = models.CharField(max_length=5000)

   def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/cuisine/%s/" % url_name

   def __str__ (self):
        return self.full_name
#-------------
#Recipe Model
#-------------

class Recipes (models.Model) : 

# """ 
#  The Recipe model returns name, id (recipe name)  url,
#  cuisine, cooking method, ingredients, and image
# """

   name = models.CharField(max_length=500)
   recipe_id = models.CharField(max_length=500)
   directions = models.CharField(max_length= 5000, default = "")
   cuisine = models.ForeignKey(Cuisines)
   ingredients = models.ManyToManyField("Ingredients", default = "")
   # How to put ingredients into list?? I think there's models.ManytoMany ?
   img = models.CharField(max_length=500)
   nut_info = models.CharField(max_length=5000)
   quant_data = models.CharField(max_length=500)


   def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/Recipes/%s/" % url_name

   def __str__ (self):
        return self.full_name
  



