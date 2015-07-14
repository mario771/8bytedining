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

    url(r'^Index1$', views.Index1, name='Index1'),
    url(r'^Index2$', views.Index2, name='Index2'),
    url(r'^recipe_page$', views.recipe_page, name='recipe_page'),
    url(r'^cuisine_page$', views.cuisine_page, name='cuisine_page'),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 
]

urlpatterns = format_suffix_patterns(urlpatterns)
 
