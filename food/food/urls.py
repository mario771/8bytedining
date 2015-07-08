"""food URL Configuration

"""

from django.conf.urls import include, url
from django.contrib import admin
from foodApp import views


urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home,name='home'),
      
    url(r'^Ingredients$', views.Ingredients, name='Ingredients'),
    url(r'^Recipes$', views.Recipes, name='Recipes'),
    url(r'^Cuisines$', views.Cuisines, name='Cuisines'),

    
    
] 
