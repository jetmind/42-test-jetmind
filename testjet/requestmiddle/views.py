# Create your views here.
from testjet.requestmiddle.models import StoredHttpRequest
from testjet.requestmiddle.forms import RequestPriorityForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def request_list(request, template_name='request_list.html'):

    if request.method == 'POST':
        rid = request.POST['requestid']
        try:
            req = StoredHttpRequest.objects.get(pk=rid)
            form = RequestPriorityForm(request.POST, instance=req)
            if form.is_valid():
                form.save()

        except StoredHttpRequest.DoesNotExist:
            form = RequestPriorityForm(request.POST)

    else:
        form = RequestPriorityForm()

    req_list = StoredHttpRequest.objects.all().order_by('-priority', '-created_at')[:10]

    return render_to_response(template_name, {
        'request_list': req_list,
        'form': form,
        }, context_instance=RequestContext(request))
