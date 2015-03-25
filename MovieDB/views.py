

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


#class IndexTemplate(TemplateView):
#    template_name = "index_class.html"
#    def get_context_data(self, **kwargs):
#        context = super(IndexTemplate, self).get_context_data(**kwargs)
#        context['name'] = 'Parikshit'
#        return context



def results(request, movie_id):
    data = Movie.objects.get(id=movie_id)
    title = data.title
    return render_to_response('results.html', {"movie_title": title})


def add_movie_form(request):
    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
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


