from django.conf.urls.defaults import *

urlpatterns = patterns('testjet.requestmiddle.views',
    (r'', 'request_list', {'template_name': 'request_list.html'}, 'request_list'),
)
