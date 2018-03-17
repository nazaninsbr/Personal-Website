from django.shortcuts import render
from django.views import generic 
from . import models

class ViolinBlog(generic.ListView):
	queryset = models.Entry.objects.published()
	template_name = "./violin.html"

def postList(request):
	wb = ViolinBlog()
	return render(request, wb.template_name, {'queryset':wb.queryset})