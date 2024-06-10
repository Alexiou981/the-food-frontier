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

@admin.register(RecipeComment)
class RecipeCommentAdmin(SummernoteModelAdmin):

    list_display = ('body', 'approval_status')
    search_fields = ['body']
    list_filter = ('approval_status',)
    summernote_fields = ('body',)
