from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin
from .forms import RecipeForm


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'cuisine', 'status')
    search_fields = ['title']
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        """
        Function ensures that the author is assigned as logged in user
        for new recipes.
        Code taken from here:
        https://djangopatterns.readthedocs.io/en/latest/models/automatically_filling_user.html
        """
        if not obj.author.id:
            obj.author = request.user
        obj.save()
