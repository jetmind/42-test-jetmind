# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from testjet.contact.models import Person

def index_view(request, template_name='index.html'):
    p = get_object_or_404(Person, pk=1)

    return render_to_response(template_name, {'person': p},
            context_instance=RequestContext(request))
