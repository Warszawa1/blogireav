from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.BinaryField(editable=True, blank=True, null=True)
    image_small = models.BinaryField(blank=True, null=True)
    image_medium = models.BinaryField(blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(BytesIO(self.image))

            # Create small image (mobile)
            small_size = (400, 225)  # 16:9 aspect ratio
            small_img = img.copy()
            small_img.thumbnail(small_size, Image.LANCZOS)
            small_buffer = BytesIO()
            small_img.save(small_buffer, format='JPEG')
            self.image_small = small_buffer.getvalue()

            # Create medium image (tablet)
            medium_size = (800, 450)
            medium_img = img.copy()
            medium_img.thumbnail(medium_size, Image.LANCZOS)
            medium_buffer = BytesIO()
            medium_img.save(medium_buffer, format='JPEG')
            self.image_medium = medium_buffer.getvalue()

            # Resize original image (desktop)
            large_size = (1200, 675)
            img.thumbnail(large_size, Image.LANCZOS)
            large_buffer = BytesIO()
            img.save(large_buffer, format='JPEG')
            self.image = large_buffer.getvalue()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"