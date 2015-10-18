from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	template = 'index.html'
	context_dict = {}
	return render(request, template, context_dict)

def jquery_ajax(request):
	# return HttpResponse('dasdasdqwe')
	if request.method == 'POST':
		print "DEAN"
		print request.POST
	template = 'extras/jquery_ajax_post_capture_name_value_pair.html'
	context_dict = {}
	return render(request, template, context_dict)