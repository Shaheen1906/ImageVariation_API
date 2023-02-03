import os
from urllib import request
from rest_framework import viewsets
from .models import *
from .serializers import *
from PIL import Image 
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageVariation.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return ImageVariation.objects.filter(user=self.request.user)
      
    def perform_create(self, serializer):
      image = self.request.FILES['image']
      
      pillow_image = Image.open(image)
      
      serializer.validated_data['user'] = self.request.user
      instance = serializer.save()
      id = instance.id

    # Generate Thumbnail
      pillow_image = pillow_image.resize((200, 300))
      thumbnail = self._generate_image_path(id, image.name, 'thumbnail')
      os.makedirs(os.path.dirname(thumbnail), exist_ok=True)
      pillow_image.save(thumbnail)
    
    # Generate Medium
      pillow_image = pillow_image.resize((500, 500))
      medium = self._generate_image_path(id, image.name, 'medium')
      os.makedirs(os.path.dirname(medium), exist_ok=True)
      pillow_image.save(medium)
    
    # Generate Large
      pillow_image = pillow_image.resize((1024, 768))
      large = self._generate_image_path(id, image.name, 'large')
      os.makedirs(os.path.dirname(large), exist_ok=True)
      pillow_image.save(large)
    
    # Generate Grayscale
      pillow_image = pillow_image.resize((500, 500))
      grayscale = self._generate_image_path(id, image.name, 'grayscale')
      os.makedirs(os.path.dirname(grayscale), exist_ok=True)
      pillow_image.convert('L').save(grayscale)

    # Save image paths in serializer
      serializer.validated_data['thumbnail'] = thumbnail
      serializer.validated_data['medium'] = medium
      serializer.validated_data['large'] = large
      serializer.validated_data['grayscale'] = grayscale

    # Call the parent create method to save the Image instance
      super().perform_create(serializer)

    def _generate_image_path(self, id, filename, size):
      return os.path.join('images', str(id), size, filename)
