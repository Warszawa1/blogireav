from django.contrib import admin
from django.db import models
from .models import Post, Comment
from .forms import PostForm

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/blog/custom_change_form.html'
    form = PostForm

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

