# Create your views here.

from django.template import Context
from django.shortcuts import render
from msuite_app.models import Project, Developer
import datetime


# Landing Page
# gives list of latest projects, and list of all other projects
# to the template 'home.html'
def landing(request):
	# query database for list of all projects
	projs_list = Project.objects.all().order_by('-date_published')
		
	# create context to pass to the template
	c = Context( {
		'projects_list' : projs_list,
	} )
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
	
	like_liked = "Like"
	# query database for the project object specified in the url. raise 404 if object does not exist
	project = Project.objects.get(id=proj_id)
	# list of developers on the project
	developers_list = [ project.developer ]
	# text for like button
	if (request.method == 'POST'):
		like_liked = "Liked"
	
	# create context to pass to the template
	c = Context( {
		'project' : project,
		'developers_list' : developers_list,
		'like_liked': like_liked,
	} )
	return render(request, 'msuite_app/projDetails.html', c)

