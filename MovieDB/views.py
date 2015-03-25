

# Create your views here.
from django.shortcuts import render_to_response, render
from forms import MovieForm
from MovieDB.models import Movie
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import context
from django.template.loader import get_template
from django.views.generic.base import TemplateView

def home(request):
    return render(request, 'index.html')


def index(request):
    return render_to_response('index.html')


def results(request, movie_id):
    data = Movie.objects.get(id=movie_id)
    title = data.title
    return render_to_response('results.html', {"movie_title": title})


def add_movie_form(request):
    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
            # Check if the movie already exists in the database
            check_db = Movie.objects.filter(title=request.POST['title'])
            if len(check_db) > 0:
                return render(request, 'movie_exists.html', {'movie_title': request.POST['title']})
            else:
                form.save()
                return HttpResponseRedirect('.')
    else:
        form = MovieForm()
    return render(request, 'add_movie_form.html',
                  {'form': form})


def search(request, movie_title):
    return render_to_response('search.html')


def add_success(request, movie_id):
    return render_to_response('add_success.html')


