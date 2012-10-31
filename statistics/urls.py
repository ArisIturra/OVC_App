

from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
        #(r'^(?P<station>\w{0,4})/(?P<datee>)\d+/', 'Aditional_Rest.views.details'),
        (r'^(?P<data>\w{15,20})/$', 'statistics.views.auto'),
)


