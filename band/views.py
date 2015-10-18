from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from . serializers import BandSerializer
from . models import Band

# Create your views here.
def all_bands(request):
	template = 'band/all_bands.html'
	context_dict = {}
	return render(request, template, context_dict)

# http://www.django-rest-framework.org/api-guide/generic-views/
# One of the key benefits of class based views is the way they allow you to compose bits of reusable behavior
# The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.
class BandDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer

def band(request, band_id):
	try:
		band = Band.objects.get(id=band_id)
	except:
		return HttpResponse('Band not available')

	template = 'band/band.html'
	context_dict = {}
	context_dict['band'] = band
	return render(request, template, context_dict)