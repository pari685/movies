from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'movies.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'MovieDB.views.index'),
                       url(r'^(?P<movie_id>\d+)/results/$', 'MovieDB.views.results'),
                       url(r'^listmovie/$', 'MovieDB.views.list_all'),
                       url(r'^addmovieform/$', 'MovieDB.views.add_movie_form'),
                       url(r'^searchmovie/$', 'MovieDB.views.search'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
