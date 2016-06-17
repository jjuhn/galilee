"""
WSGI config for GalileeChurchWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application


# calculate the path based on the location of the WSGI script.
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

sys.path.append('/home/bk/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'GalileeChurchWeb.apache.override'

application = get_wsgi_application()



#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GalileeChurchWeb.settings")
#os.environ["DJANGO_SETTINGS_MODULE"] = "GalileeChurchWeb.settings"
#application = get_wsgi_application()
