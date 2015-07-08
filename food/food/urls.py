"""food URL Configuration

"""

from django.conf.urls import include, url
from django.contrib import admin
from foodApp import views


urlpatterns = [
    url(r'^potroast$',views.potroast, name='potroast'),
    url(r'^admin/', include(admin.site.urls)),
        
    
] 
