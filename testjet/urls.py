from django.conf.urls.defaults import *
from django.contrib import admin
from testjet import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testjet/', include('testjet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^requests/', include('testjet.requestmiddle.urls')),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, 'login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, 'logout'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_DOC_ROOT}, 'static'),
    (r'', include('testjet.contact.urls')),
)
