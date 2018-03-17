from django.shortcuts import render
from django.views import generic 
from . import models

class WorkoutBlog(generic.ListView):
	queryset = models.Entry.objects.published()
	template_name = "workout.html"

def postList(request):
	wb = WorkoutBlog()
	return render(request, wb.template_name, {'queryset':wb.queryset})