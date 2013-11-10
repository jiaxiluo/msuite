from msuite_app.models import Project, Developer
from django.contrib import admin

class Admin(admin.ModelAdmin):
	list_display = ('name', 'id')

admin.site.register(Project, Admin)
admin.site.register(Developer, Admin)


