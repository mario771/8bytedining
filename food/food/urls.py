"""food URL Configuration

"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$',include('foodApp.urls')),
    url(r'^foodApp/',include('foodApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
]
