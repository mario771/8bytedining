from django.contrib import admin

from .models import Recipes
from .models import Ingredients
from .models import Cuisine

admin.site.register(Recipes)
admin.site.register(Ingredients)
admin.site.register(Cuisine)




