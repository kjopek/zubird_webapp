from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
admin.autodiscover()

from contact.views import index,send

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zubird.views.home', name='home'),
    # url(r'^zubird/', include('zubird.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^send/', send),
    url(r'^$', index),
    
)
