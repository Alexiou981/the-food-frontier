from django.contrib import admin
from .models import Recipe, RecipeComment

# Register your models here.

admin.site.register(Recipe)
admin.site.register(RecipeComment)