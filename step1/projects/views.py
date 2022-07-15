from django.shortcuts import render
from .models import Project

def projects(request):
	projects = Project.objects.all()
	context = {'projects': projects}

	return render(request, 'projects/projects.html', context)

def project(request, pk):
	projectObj = Project.objects.get(id=pk)
	tags = projectObj.tags.all()

	return render(request, 'projects/single-project.html', {'project': projectObj})