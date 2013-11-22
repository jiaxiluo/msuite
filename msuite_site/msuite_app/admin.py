from msuite_app.models import Project, Developer
from django.contrib import admin


# amdin model class to display Project info in admin site
class ProjectAdmin(admin.ModelAdmin):
	# displays these fields for each Project by default
	list_display = ('name', 'id', 'sponsor_name', 'date_published')
	# choice to filter by these fields
	#list_filter = ('name', 'id', 'sponsor_name', 'date_published')
	#date_hierarchy = 'date_published'
	# Projects are searchable by these fields
	#search_fields = ('name', 'id', 'sponsor_name', 'date_published') 

# class to display Developer info in admin site
class DeveloperAdmin(admin.ModelAdmin):
	# displays these fields for each Developer by default
	list_display = ('last_name', 'first_name', 'id', 'email')
	# choice to filter by these fields
	#search_fields = ('last_name', 'first_name', 'id', 'email') 


# register our models with the admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(Developer, DeveloperAdmin)

