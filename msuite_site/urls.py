from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from msuite_app.views import home, developers, projDetails

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'msuite_site.views.home', name='home'),
    # url(r'^msuite_site/', include('msuite_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', home),
	url(r'^developers/$', developers),
	url(r'^(?P<proj_id>\w+)/$', projDetails),
	url(r'^images/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), 
)
