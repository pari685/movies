from django.db import models
from django.contrib import admin

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)

class ItemAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

admin.site.register(Movie, ItemAdmin)