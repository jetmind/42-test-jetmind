from testjet.contact.models import Person, Contacts
from testjet.contact.widget import CalendarWidget
from django import forms

class PersonEditForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('bio', 'birth', 'surname', 'name')
        widgets = {
                'birth': CalendarWidget,
        }

class ContactsEditForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('other', 'jabber', 'email')

