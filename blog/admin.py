from django.contrib import admin
from .models import Post, PostComment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('content',)


@admin.register(PostComment)
class PostCommentAdmin(SummernoteModelAdmin):

    list_display = ('post', 'body')
    search_fields = ['body']
    list_filter = ('approval_status',)
    summernote_fields = ('body',)

