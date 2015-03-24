__author__ = 'pjuluri'

from django import forms
from models import Movie

"""
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.FloatField()
    director = models.CharField(max_length=200)


"""

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = {"title", "release_date", "director", "rating"}


