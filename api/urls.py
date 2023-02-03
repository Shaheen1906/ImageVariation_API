# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
    
# ]
import statistics
from django.urls import path, include
# from .views import ImageViewSet

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'images', ImageViewSet)

from rest_framework import routers
from .views import ImageViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')

urlpatterns = [
    # ...
    path('', include(router.urls)),
    # ...
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
