from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photographer')
    image = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=255, blank=True)
    is_approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id.username}'s photo"


class GalleryPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
