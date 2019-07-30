from django.shortcuts import render
from projects.models import Project


def index_page(request):
	projects=Project.objects.all()
	context={
		'projects':projects
	}

	return render(request, 'index_page.html',context)


def project_detail(request, pk):
	project_detail=Project.objects.get(pk=pk)
	context={
		'project':project_detail
	}
	return render(request, 'detail_page.html', context)





# Create your views here.
