from django.contrib import admin
from .models import *

@admin.register(ImageVariation)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image','user')