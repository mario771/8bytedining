from django.contrib import admin

from .models import Recipes
from .models import Ingredients
from .models import Cusine

admin.site.register(Recipes)
admin.site.register(Ingredients)
admin.site.register(Cusine)




