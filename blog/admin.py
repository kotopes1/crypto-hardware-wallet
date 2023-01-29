"""
This script imports the necessary modules to create and manage the posts and
and comment models in the django admin interface.
The admin module is imported from 'django.contrib' and is used to register the
models with the admin interface.
The 'summernotemodeladmin' module is imported from
'django_summernote.admin' and is used as the base class for custom admin
class'postadmin' and 'commentadmin' to allow using summernote wysiwyg
editor in admin interface.
finally, the 'post' and 'comment' models are imported from the current package,
and are registered with the admin interface using the custom admin classes
'postadmin' and 'commentadmin'
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    For posts in blog
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This script is a custom admin class for comment model, which allows for
    additional functionality in the django admin interface when managing
    comments.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
Approve the selected comments.
Args:
        request (HttpRequest): The current request object.
        queryset (QuerySet): The selected comments to approve.
Returns:
        None
    """
        queryset.update(approved=True)
