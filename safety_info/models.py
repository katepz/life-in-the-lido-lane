from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class SafetyInfo(models.Model):
    title = models.CharField(max_length=255)
    safety_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title