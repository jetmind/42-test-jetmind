from django.conf.urls.defaults import *

urlpatterns = patterns('testjet.contact.views',
    (r'^edit/$', 'edit_view', {'template_name': 'edit.html'}, 'edit'),
    (r'', 'index_view', {'template_name': 'index.html'}, 'index'),
)
