from django.shortcuts import render
from projects.models import Project


def project_index(request):
	context = {
		'projects': Project.manager.get_all()
	}
	return render(request, 'project_index.html', context)


def project_detail(request, pk):
	context = {
		'project': Project.manager.get(pk=pk)
	}
	return render(request, 'project_detail.html', context)
