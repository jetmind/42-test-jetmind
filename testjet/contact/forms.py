from testjet.contact.models import Person, Contacts
from django import forms

class PersonEditForm(forms.ModelForm):
    class Meta:
        model = Person

class ContactsEditForm(forms.ModelForm):
    class Meta:
        model = Contacts
        exclude = ('person', )
