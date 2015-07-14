from django.db import models

# Create your models here.

#------------------
#Ingredients Model
#------------------

class Ingredients (models.Model) :
   ing_id = models.CharField(max_length=500, default="") 
   name = models.CharField(max_length=500, default="")
 #  recipe_count = models.IntegerField(default=0)
   quant_data = models.CharField(max_length=500, default="")
   nut_info = models.CharField(max_length=5000, default="")

#   calories_from_fat= models.CharField(max_length=30,default="")
#   iron= models.CharField(max_length=30,default="")
#   protein= models.CharField(max_length=30,default="")
#   calories= models.CharField(max_length=30,default="")
#   vitamin_c= models.CharField(max_length=30,default="")
#   vitamin_a= models.CharField(max_length=30,default="")
#   sodium= models.CharField(max_length=30,default="")
#   fat= models.CharField(max_length=30,default="")
#   calcium= models.CharField(max_length=30,default="")
#   cholesterol= models.CharField(max_length=30,default="")
#   trans_fat= models.CharField(max_length=30,default="")
#   saturated_fat= models.CharField(max_length=30,default="")
#   carbohydrates= models.CharField(max_length=30,default="")
#   diveristy= models.CharField(max_length=30,default="")
#   calories_per_100g= models.CharField(max_length=30,default="")
#   popularity= models.CharField(max_length=30,default="")
#   number_of_cuisines= models.CharField(max_length=30,default="")
#   number_of_recipes= models.CharField(max_length=30,default="")
  
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
   id_cuisine = models.CharField(max_length=500)
   name = models.CharField(max_length=500)
   url = models.CharField(max_length=500)
   #recipe_count = models.IntegerField(default=0)
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
   #cuisine = models.ForeignKey(Cuisines)
   cuisine = models.ForeignKey(Cuisines)
   ingredients = models.ManyToManyField("Ingredients", default = "")
   ingredient_amount = models.CharField(max_length= 2000, default = "")
   # How to put ingredients into list?? I think there's models.ManytoMany ?
   img = models.CharField(max_length=500)
   nut_info = models.CharField(max_length= 5000, default = "")
   quant_data = models.CharField(max_length=500)
#    "quant_data": 
#       "{"diveristy": 3.0303030303030303,
#       "calories_per_100g": "81.0 kcal per 100g ",
#       "popularity": 0.2,
#       "number_of_cuisines": 1,
#       "number_of_recipes": 1}",


   def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/Recipes/%s/" % url_name

   def __str__ (self):
        return self.full_name
  



