from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns('',
	url(r'^$', views.all_bands),
	url(r'^(?P<band_id>\d+)/$', views.band),
	url(r'^api/(?P<pk>[0-9]+)/$', views.BandDetail.as_view()),
	)

# http://www.django-rest-framework.org/api-guide/format-suffixes/#format_suffix_patterns
# Chris Hawkes: allows us to request the api
# Personal Instruction: Try 127.0.0.1:8000/band/api/1.json on the url address to test effects (comment and uncomment line below)
urlpatterns = format_suffix_patterns(urlpatterns)