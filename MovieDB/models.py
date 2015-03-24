from django.db import models
from django.contrib import admin

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.FloatField()
    director = models.CharField(max_length=200)

class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "release_date", "rating", "director"]
    search_fields = ["title"]

admin.site.register(Movie, ItemAdmin)