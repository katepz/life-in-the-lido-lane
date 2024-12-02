from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class SafetyInfo(models.Model):
    title = models.CharField(max_length=255)
    safety_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SafetySuggestion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lifesaver')
    name = models.CharField(max_length=255)
    tip = models.TextField()
    is_approved = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Safety tip from {self.name}"