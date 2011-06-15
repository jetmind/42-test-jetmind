# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from testjet.contact.models import Person
from testjet.contact.forms import PersonEditForm, ContactsEditForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index_view(request, template_name='index.html'):
    p = get_object_or_404(Person, pk=1)

    return render_to_response(template_name, {'person': p},
            context_instance=RequestContext(request))

@login_required
def edit_view(request, template_name='edit.html'):
    p = get_object_or_404(Person, pk=1)
    c = p.contacts

    if request.method == 'POST':
        person_form = PersonEditForm(request.POST)
        contacts_form = ContactsEditForm(request.POST)

        if person_form.is_valid() and contacts_form.is_valid():
            p.name = person_form.cleaned_data['name']
            p.surname = person_form.cleaned_data['surname']
            p.birth = person_form.cleaned_data['birth'] 
            p.bio = person_form.cleaned_data['bio']

            c.email = contacts_form.cleaned_data['email']
            c.jabber = contacts_form.cleaned_data['jabber'] 
            c.other = contacts_form.cleaned_data['other']

            p.save()
            c.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        person_form = PersonEditForm(instance=p)
        contacts_form = ContactsEditForm(instance=c)

    return render_to_response(template_name, {'person_form': person_form,
        'contacts_form': contacts_form}, context_instance=RequestContext(request))
