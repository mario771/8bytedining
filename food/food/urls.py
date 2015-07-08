"""food URL Configuration

"""

from django.conf.urls import include, url
from django.contrib import admin
from foodApp import views


urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home,name='home'),
      
    url(r'^American$', views.American, name='American'),
#    url(r'^PotRoast$', views.Aunt_Ruthie_Pot_Roast, name='Aunt_Ruthie_Pot_Roast'),
    url(r'^Cuisines$', views.Cuisines, name='Cuisines'),
        
    url(r'^Indian$', views.Indian, name='Indian'),
    url(r'^Ingredients$', views.Ingredients, name='Ingredients'),
    url(r'^Italian$', views.Italian, name='Italian'),
    url(r'^Naan$', views.Naan, name='Naan'),
    url(r'^Recipes$', views.Recipes, name='Recipes'),
    url(r'^Cuisines$', views.Cuisines, name='Cuisines'),

    url(r'^Risotto_Milanese$', views.Risotto_Milanese, name='Risotto_Milanese'),
    url(r'^Bread_Flour$', views.Bread_Flour, name='Bread_Flour'),
    url(r'^Light_BrownSugar$', views.Light_Brown_Sugar, name='Light_Brown_Sugar'),
    url(r'^Parmesan_Cheese$', views.Parmesan_Cheese, name='Parmesan_Cheese'),
    
] 
