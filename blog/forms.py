from django import forms
from .models import Comment, Post
import base64

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
        }


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['author'].widget = forms.HiddenInput()
    #
    # def save(self, commit=True):
    #     instance = super(PostForm, self).save(commit=False)
    #     image = self.cleaned_data.get('image')
    #
    #     if image:
    #         if isinstance(image, memoryview):
    #             # If it's already a memoryview, just assign it
    #             instance.image = image
    #         else:
    #             # If it's a new file upload, read it
    #             instance.image = image.read()
    #         instance.image_name = getattr(image, 'name', None)
    #     elif self.cleaned_data.get('image') is False:
    #         # If the image is explicitly cleared in the form
    #         instance.image = None
    #         instance.image_name = None
    #
    #     if commit:
    #         instance.save()
    #     return instance