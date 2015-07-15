"""food URL Configuration

"""

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include, url
from django.contrib import admin
from foodApp import views
from foodApp import api
   

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home,name='home'),
    url(r'^about$', views.about, name='about'),
    #recipes/model is going to be the model page
    

    #Recipe
    url(r'^recipes/(?P<r_name>[-\w]+)/$', views.recipe, name='recipe'),
    url(r'^recipes$', views.recipes, name='recipes'),

    
    #Ingredients 
    url(r'^ingredients/(?P<i_name>[-\w]+)/$', views.ingredient, name='ingredient'),
    url(r'^ingredients$', views.ingredients, name='ingredients'),
   
    #Cuisine 
    url(r'^cuisines/(?P<c_name>[-\w]+)/$', views.cuisine, name='cuisine'),
    url(r'^cuisines$', views.cuisines, name='cuisines'),
    
    
    #API URLs
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^api/recipes/$',api.RecipeList.as_view()),
    url(r'^api/recipes/(?P<pk>[0-9]+)/$', api.RecipeDetail.as_view()),

    url(r'^api/cuisines/$',api.CuisineList.as_view()),
    url(r'^api/cuisines/(?P<pk>[-\w]+)/$', api.CuisineDetail.as_view()),

    url(r'^api/ingredients/$',api.IngredientList.as_view()),
    url(r'^api/ingredients/(?P<pk>[-\w]+)/$', api.IngredientDetail.as_view()),

   
]

urlpatterns = format_suffix_patterns(urlpatterns)
 
