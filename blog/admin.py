from django.contrib import admin
from django.db import models
from .models import Post, Comment

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/blog/custom_change_form.html'

    # list_display = ('title', 'author', 'created_at', 'updated_at')
    # search_fields = ('title', 'content')
    # list_filter = ('created_at', 'updated_at')
    # date_hierarchy = 'created_at'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

