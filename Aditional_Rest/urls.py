from django.conf.urls.defaults import *
from django.conf import settings
import colors

urlpatterns = patterns('',
	(r'^$', 'Aditional_Rest.views.details'),
)
	
