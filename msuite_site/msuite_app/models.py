from django.db import models
from djangotoolbox import fields
from .forms import StringListField

class CategoryField(fields.ListField):
	def formfield(self, **kwargs):
		return models.Field.formfield(self, StringListField, **kwargs)


class Project(models.Model):
	name = models.CharField(max_length=100)
	developers_ids = CategoryField()
	developers_names = CategoryField()
	semester = models.CharField(max_length=100)
	platforms = CategoryField()
	description = models.TextField()
	date = models.DateTimeField('date published')
	image = models.FileField("Project Image", upload_to="projects")

	def __unicode__(self):
		return self.name
	

class Developer(models.Model):
	name = models.CharField(max_length=100)
	majors = CategoryField()
	projects_ids = CategoryField()
	projects_names = CategoryField()
	bio = models.TextField()
	status = models.CharField(max_length=100)
	image = models.FileField(upload_to="developers")

	def __unicode__(self):
		return self.name

