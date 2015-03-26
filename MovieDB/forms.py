""" Module with the MovieForm class"""
__author__ = 'pjuluri'

from django import forms
from models import Movie

class MovieForm(forms.ModelForm):
    """ Movie Form """
    class Meta:
        """ Assigning the order of the fields"""
        model = Movie
        fields = ["title", "director", "genre", "language"]


