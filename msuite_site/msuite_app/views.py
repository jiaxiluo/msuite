# Create your views here.

from django.template import Context, RequestContext
from django.shortcuts import render
from msuite_app.models import Project, Developer
import datetime


# Landing Page
# gives list of latest projects, and list of all other projects
# to the template 'home.html'
def landing(request):
	# find order in request.POST
	if 'order' in request.POST:
		order = request.POST['order']
		request.session['order'] = order
	# find order in session
	elif 'order' in request.session:
		order = request.session['order']
	# default
	else: 
		order = 'newest'

	# query database for list of all projects
	if order == 'abc':
		projs_list = Project.objects.all().order_by('name')
	elif order == 'oldest':
		projs_list = Project.objects.all().order_by('date_published')
	else:
		projs_list = Project.objects.all().order_by('-date_published')
		
	# create context to pass to the template
	c =  RequestContext( request, 
		{
		'projects_list' : projs_list,
		'order' : order,
		} 
	)
	# render the template with the given context
	return render(request, 'msuite_app/landing.html', c)


# Developers Page
# gives list of developers to the template 'developers.html'
def developers(request):
	# query database for list of all developers
	developers_list = Developer.objects.all().order_by('-last_name')
	# create context to pass to the template
	c = Context( {
		'developers_list' : developers_list,
	} )
	return render(request, 'msuite_app/developers.html', c)
	

# Project Details Page
# gives a project object and a list of developers on the project to
# the template 'projDetails.html'
# the project to give is determined by the project id in the url
def projDetails(request, proj_id):
	# query database for the project object specified in the url. raise 404 if object does not exist
	project = Project.objects.get(id=proj_id)

	# find like of current project in session
	if (proj_id, 'like') in request.session and request.session[(proj_id, 'like')] == 1:
		like = 1
	# find like in request.POST
	elif 'like' in request.POST:
		like = request.POST['like']
		request.session[(proj_id, 'like')] = 1 # True
		project.likes += 1;
		project.save()
	# default
	else: 
		like = 0 # false

	if 'comment' in request.POST:
		project.comments.append(request.POST['comment'])
		project.save()

	# list of developers on the project
	developers_list = [ project.developer0, project.developer1, project.developer2, project.developer3, project.developer4 ]
	
	# create context to pass to the template
	c =  RequestContext( request,
		{
		'project' : project,
		'developers_list' : developers_list,
		'like': like,
	} )
	return render(request, 'msuite_app/projDetails.html', c)

