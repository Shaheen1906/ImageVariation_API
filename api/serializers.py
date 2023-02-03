from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



      
        

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageVariation
        fields = ('id', 'user','image','thumbnail', 'medium', 'large', 'grayscale')

 