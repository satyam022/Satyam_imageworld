from django.contrib import admin
from .models import World


# Register your models here.

@admin.register(World)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'date']
