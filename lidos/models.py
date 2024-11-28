from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Lido(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length= 255, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lido_cards")
    lido_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    highlight = models.TextField
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    website = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.name