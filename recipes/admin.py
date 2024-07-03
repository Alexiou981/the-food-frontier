from django.contrib import admin
from .models import Recipe, RecipeComment
from django_summernote.admin import SummernoteModelAdmin
from .forms import RecipeForm

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'cuisine', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('instructions', 'ingredients', 'excerpt')


# Code taken from here:
# https://djangopatterns.readthedocs.io/en/latest/models/automatically_filling_user.html
    def save_model(self, request, obj, form, change):
        if not obj.author.id:
            obj.author = request.user
        obj.save() 
    
@admin.register(RecipeComment)
class RecipeComment(SummernoteModelAdmin):

    list_display = ('body', 'approval_status')
    list_filter = ('approval_status',)


