from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)



class ImageVariation(models.Model):
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    medium = models.CharField(max_length=255, blank=True)
    large = models.CharField(max_length=255, blank=True)
    grayscale = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
