

# Create your views here.
from django.shortcuts import render_to_response
from forms import MovieForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


def index(request):
    return render_to_response('index.html')


def results(request, movie_id):
    return render_to_response('results.html', {"movie_id": movie_id})


def new_movie(request):
    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/moviedb/all')
    else:
        form = MovieForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('new_movie.html', args)