"""food URL Configuration

"""

from django.conf.urls import include, url
from django.contrib import admin
from foodApp import views


urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home,name='home'),
      
    url(r'^IngredientModel$', views.IngredientsModel, name='IngredientsModel'),
    url(r'^RecipeModel$', views.Recipes, name='Recipes'),
    url(r'^CuisineModel$', views.Cuisines, name='Cuisines'),
    url(r'^Ingredients$', views.Ingredients, name='Ingredients'),
    
    
] 
