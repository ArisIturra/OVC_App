import os
import sys
import site

sys.stdout = sys.stderr
ve_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib/python2.6/site-packages"))

site.addsitedir(ve_path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
sys.path.insert(0, ve_path)
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

