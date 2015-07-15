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

    url(r'^recipes/model$', views.model, name='recipes/model'),
    url(r'^ingredients/model$', views.model, name='ingredients/model'),
    url(r'^cuisines/model$', views.model, name='cuisines/model'),

    url(r'^recipes$', views.recipe_page, name='recipes'),
    url(r'^ingredients$', views.ingredient_page, name='ingredients'),
    url(r'^cuisines$', views.cuisine_page, name='cuisines'),
    
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^api/recipes/$',api.RecipeList.as_view()),
    url(r'^api/recipes/(?P<pk>[0-9]+)/$', api.RecipeDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)
 
