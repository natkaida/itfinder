from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag
from .forms import ProjectForm

def projects(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, 'projects/projects.html', context)

def project(request, project_slug):
	project = Project.objects.get(slug=project_slug)
	tags = project.tags.all()
	return render(request, 'projects/single-project.html', {'project': project})

def createProject(request):
	form = ProjectForm()
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('projects')
	context = {'form': form}
	return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
	project = Project.objects.get(id=pk)
	form = ProjectForm(instance=project)
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return redirect('projects')
	context = {'form': form}
	return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
	project = Project.objects.get(id=pk)
	if request.method == 'POST':
		project.delete()
		return redirect('projects')
	context = {'object': project}
	return render(request, 'projects/delete.html', context)

def projects_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    projects = Project.objects.filter(tags__in=[tag])
    context = {
        "projects": projects
    }

    return render(request, "projects/projects.html", context)
