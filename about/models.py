from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    about_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Suggestion(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    lido_idea = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Lido suggestion from {self.name}"