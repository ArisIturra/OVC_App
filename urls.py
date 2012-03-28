from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OVC_App.views.home', name='home'),
    # url(r'^OVC_App/', include('OVC_App.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^$',redirect_to, {'url': '/admin'}),
     url(r'^admin/', include(admin.site.urls)),

)
urlpatterns += staticfiles_urlpatterns()
