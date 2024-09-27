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

