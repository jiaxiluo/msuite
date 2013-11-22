from django.db import models
from djangotoolbox import fields
from .forms import StringListField
from django import forms


# subclass of a ListField for use in admin site
class CategoryField(fields.ListField):
	def formfield(self, **kwargs):
		return models.Field.formfield(self, StringListField, **kwargs)


# represenation of a developer person
class Developer(models.Model):
	# name of the developer
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	# what is the developer's major
	major = models.CharField(max_length=100, blank=True)
	# paragraph biography of the developer
	bio = models.TextField()
	# developer's email address
	email = models.EmailField()
	# image to be displayed for the developer
	image = models.FileField("Developer Image", blank=True, upload_to="images/developers/")
	# not sure what this is
	status = models.CharField(max_length=100)
	# what projects the developer is working on / has worked on
	project0 = models.ForeignKey('Project', blank=True, null=True, related_name='+')
	project1 = models.ForeignKey('Project', blank=True, null=True, related_name='+')
	project2 = models.ForeignKey('Project', blank=True, null=True, related_name='+')
	project3 = models.ForeignKey('Project', blank=True, null=True, related_name='+')
	project4 = models.ForeignKey('Project', blank=True, null=True, related_name='+')

	# class that contains options specific to this model
	class Meta:
		# default ordering
		ordering = ['last_name']
	
	def __unicode__(self):
		return u'%s, %s %s' %(self.last_name, self.first_name, self.id)


	

# testing for multiple developers
#DEVELOPERS = ()
#DEVELOPERS = Developer.objects.all().order_by('-last_name')
#class DevelopersField(fields.ListField):
#	def formfield(self, **kwargs):
#		return models.Field.formfield(self, MultipleChoiceField, **kwargs)



# represenation of a project
class Project(models.Model):
	# name of project
	name = models.CharField(max_length=100)
	# date project was published
	date_published = models.DateTimeField('date published')
	# not sure what this is
	semester = models.CharField(max_length=100)
	# mobile platforms used by the projects, e.g., Android, iOS
	platforms = CategoryField(blank=True)
	# is the project a paid opportunity
	#paid = models.CharField(max_length=10, verbose_name='paid project')
	# image to be displayed for the project
	image = models.FileField("Project Image", upload_to="images/projects/", blank=True)
	# how many likes the project has
	likes = models.IntegerField()
	# comments left by users
	comments = CategoryField(blank=True)
	# additional key words to improve searchability
	#tags = CategoryField(blank=True)
	# who sponsors (runs) the project
	sponsor_name = models.CharField(max_length=50)
	sponsor_website = models.URLField(blank=True)
	# developer working on the project
	developer0 = models.ForeignKey('Developer', blank=True, null=True, related_name='+')
	developer1 = models.ForeignKey('Developer', blank=True, null=True, related_name='+')
	developer2 = models.ForeignKey('Developer', blank=True, null=True, related_name='+')
	developer3 = models.ForeignKey('Developer', blank=True, null=True, related_name='+')
	developer4 = models.ForeignKey('Developer', blank=True, null=True, related_name='+')
	# paragraph description of the project
	description = models.TextField()
	
	# testing multiple developers
	#developers = DevelopersField(blank=True, choices=DEVELOPERS)
	
	# class that contains options specific to this model
	class Meta:
		# default ordering
		ordering = ['date_published']
	
	def __unicode__(self):
		return u'%s %s' %(self.name, self.id)

