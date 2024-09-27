from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from bleach import clean
from django.utils.html import mark_safe



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.BinaryField(editable=True, blank=True, null=True)

    def __str__(self):
        return self.title


    # def save(self, *args, **kwargs):
    #     if self.image:
    #         img = Image.open(self.image)
    #
    #         max_size= (1200, 675)
    #         img.thumbnail(max_size, Image.LANCZOS)
    #
    #         # Save the resized image
    #         buffer = BytesIO()
    #         img.save(buffer, format='JPEG', quality=85)  # Adjust quality as needed
    #         self.image.save(f'{self.image.name}',
    #                         ContentFile(buffer.getvalue()),
    #                         save=False)
    #
    #     super().save(*args, **kwargs)
    #
    def get_safe_content(self):
        return mark_safe(self.content)
        # Define allowed tags and attributes
        # allowed_tags = ['p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'span', 'div']
        # allowed_attributes = {'a': ['href', 'title'], 'span': ['style'], 'div': ['style']}
    #
    #     # Clean the content
    #     cleaned_content = clean(self.content, tags=allowed_tags, attributes=allowed_attributes, strip=True)
    #     return mark_safe(cleaned_content)


    # def __str__(self):
    #     return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"