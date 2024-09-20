from django.contrib import admin
from django.db import models
from .models import Post, Comment
from .forms import PostForm

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    change_form_template = 'admin/blog/post/custom_change_form.html'


    def save_model(self, request, obj, form, change):
        if not obj.pk:  # This is a new object
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

