""" Models for the Simple MOvie database"""
from django.db import models
from django.contrib import admin




class Movie(models.Model):
    """ The Movie Class
        title: The Title of the movie
        language: The Language of the movie
        Genre: Select for the list of genres
        director: Name of the director
    """
    GENRE_OPTIONS = (
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('SciFi', 'SciFi'),
        ('Action', 'Action'),
        ('Period', 'Period')
    )
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=10,
                             choices=GENRE_OPTIONS)


class ItemAdmin(admin.ModelAdmin):
    """ Used by the admin site
    """
    list_display = ["title"]
    search_fields = ["title"]

admin.site.register(Movie, ItemAdmin)
