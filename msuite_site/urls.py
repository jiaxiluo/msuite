from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from msuite_app.views import landing, developers, projDetails

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'msuite_site.views.home', name='home'),
    # url(r'^msuite_site/', include('msuite_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # landing page
	url(r'^$', landing),
	# page to list developers
	url(r'^developers/$', developers),
	# page to display details of project given the project id
	url(r'^(?P<proj_id>\w+)/$', projDetails),
	# handles media files
	url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
	# handles static files
    url(r'^static/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), 
)

