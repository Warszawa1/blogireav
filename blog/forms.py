from django import forms
from .models import Comment, Post

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
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'content': forms.Textarea(attrs={'rows': 8, 'class': 'w-full p-2 border rounded'}),
        }

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        image = self.cleaned_data.get('image')
        if image:
            instance.image = image.read()
            instance.image_name = image.name
        elif self.cleaned_data.get('image') is False:
            # If the image is explicitly cleared in the form
            instance.image = None
            instance.image_name = None
        if commit:
            instance.save()
        return instance