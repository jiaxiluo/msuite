import os
import sys	
sys.path.append('/home/jiaxiluo/')
sys.path.append('/home/jiaxiluo/msuite_site/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'msuite_site.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
