from django.conf.urls.defaults import *

urlpatterns = patterns('testjet.contact.views',
    (r'', 'index_view', {'template_name': 'index.html'}),
)
