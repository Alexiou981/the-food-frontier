from django.contrib import admin
from .models import Recipe, RecipeComment, UsersRecipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'cuisine', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('instructions', 'ingredients', 'excerpt')

@admin.register(RecipeComment)
class RecipeComment(SummernoteModelAdmin):

    list_display = ('body', 'approval_status')
    list_filter = ('approval_status',)


@admin.register(UsersRecipe)
class UsersRecipeAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'cuisine', 'ingredients', 'instructions', 'approval_status')