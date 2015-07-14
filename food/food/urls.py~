"""food URL Configuration

"""

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include, url
from django.contrib import admin
from foodApp import views

   

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home,name='home'),
    url(r'^About$', views.About, name='About'),
"""
    url(r'^IngredientModel$', views.IngredientsModel, name='IngredientsModel'),
    url(r'^RecipeModel$', views.RecipesModel, name='RecipesModel'),
    url(r'^CuisineModel$', views.CuisinesModel, name='CuisinesModel'),
    url(r'^Ingredients$', views.Ingredients, name='Ingredients'),
    url(r'^Cuisines$', views.Cuisines, name='Cuisines'),
    url(r'^Recipes$', views.Recipes, name='Recipes'),
    url(r'^American$', views.American, name='American'),
    url(r'^Italian$', views.Italian, name='Italian'),
"""
    url(r'^Index1$', views.Index1, name='Index1'),
    url(r'^Index2$', views.Index2, name='Index2'),
    url(r'^recipe_page$', views.recipe_page, name='recipe_page'),
    url(r'^cuisine_page$', views.cuisine_page, name='cuisine_page'),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 
]

urlpatterns = format_suffix_patterns(urlpatterns)
 
