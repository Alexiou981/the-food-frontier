from django.contrib import admin
from .models import Recipe, RecipeComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'cuisine', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('instructions', 'ingredients', 'excerpt')

admin.site.register(RecipeComment)
