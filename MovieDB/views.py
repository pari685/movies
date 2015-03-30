#!/usr/bin/env python
#
# A Simple Movie Database
# Copyright (C) 2015, Parikshit Juluri
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

""" The views for the Simple MOvie Database  """
from django.shortcuts import render_to_response, render
from forms import MovieForm
from MovieDB.models import Movie


def home(request):
    """ Module that returns the default home page"""
    return render(request, 'index.html')


def index(request):
    """Module that returns the index.html page"""
    return render_to_response('index.html')


def add_movie_form(request):
    """
    Module that adds the data from the page /addmovieform/
        if a movie with the same title does not exist

    :param request: request, HTML Template, movie_listing = the list of Movie objects
    :return:
    """
    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
            # Check if the movie already exists in the database
            check_db = Movie.objects.filter(title=request.POST['title'])
            if len(check_db) > 0:
                # If a movie with same name exists the do not enter to DB
                return render(request, 'movie_exists.html',
                              {'movie_title': request.POST['title']})
            else:
                # Save form and redirect to the success page
                form.save()
                return render_to_response('add_success.html',
                                          {'movie_title': request.POST['title']})
    else:
        form = MovieForm()
    return render(request, 'add_movie_form.html',
                  {'form': form})


def search(request):
    """
    Module to search the database with the title, genre, or director. Called from the /searchmovie/
    :param request: page request
    :return: request, HTML Template, movie_listing = the list of Movie objects
    """
    if request.GET:
        movie_listing = []
        search_string = ""
        # Check for each entry in the search form.
        # Find all the movies that match either one of the search entries
        if request.GET['title']:
            for movie_object in Movie.objects.filter(title__contains=request.GET['title']):
                movie_dict = {'movie_object': movie_object}
                movie_listing.append(movie_dict)
            search_string = request.GET['title']
        if request.GET['genre']:
            for movie_object in Movie.objects.filter(genre__contains=request.GET['genre']):
                movie_dict = {'movie_object': movie_object}
                movie_listing.append(movie_dict)
            search_string = " ".join((search_string, request.GET['genre']))
        if request.GET['director']:
            for movie_object in Movie.objects.filter(director__contains=request.GET['director']):
                movie_dict = {'movie_object': movie_object}
                movie_listing.append(movie_dict)
            search_string = " ".join((search_string, request.GET['director']))
        if request.GET['language']:
            for movie_object in Movie.objects.filter(language__contains=request.GET['language']):
                movie_dict = {'movie_object': movie_object}
                movie_listing.append(movie_dict)
            search_string = " ".join((search_string, request.GET['language']))
        # Redirect to the results.html page if atleast one movie is found basedon the search strings
        if len(movie_listing) > 0:
            return render_to_response('results.html', {'search_string': search_string,
                                                       'movie_listing': movie_listing})
    form = MovieForm()
    return render(request, 'search.html', {'form': form})


def list_all(request):
    """ Module to list all the movies in the database"""
    sort_by = request.GET.get('sort', 'title')
    print "Ordering by", sort_by
    movie_listing = []
    for movie_object in Movie.objects.all().order_by(sort_by):
        movie_dict = {'movie_object': movie_object}
        movie_listing.append(movie_dict)
    return render_to_response('list_all.html', {'movie_listing': movie_listing})