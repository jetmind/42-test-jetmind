# Create your views here.
from testjet.requestmiddle.models import StoredHttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext

def request_list(request, template_name='request_list.html'):
    req_list = StoredHttpRequest.objects.all().order_by('-created_at')[:10]

    return render_to_response(template_name, {'request_list': req_list},
            context_instance=RequestContext(request))
