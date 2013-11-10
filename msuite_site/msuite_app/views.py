# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from msuite_app.models import Project, Developer
import datetime

def home(request):
	projs_list = Project.objects.all().order_by('-date')
	t = loader.get_template('home.html')
	c = Context( {
		'latest_projs_list' : projs_list[0:3],
		'other_projs_list' : projs_list[4:],
	} )
	return HttpResponse(t.render(c))

def developers(request):
	developers_list = Developer.objects.all().order_by('-name')
	t = loader.get_template('developers.html')
	c = Context( {
		'developers_list' : developers_list,
	} )
	return HttpResponse(t.render(c))

def projDetails(request, proj_id):
	project = Project.objects.get(id=proj_id)
	developers_list = [ Developer.objects.get(id=dev_id) for dev_id in project.developers_ids ]
	t = loader.get_template('projDetails.html')
	c = Context( {
		'project' : project,
		'developers_list' : developers_list
	} )
	return HttpResponse(t.render(c))

