from testjet.requestmiddle.models import StoredHttpRequest
from django import forms

class RequestPriorityForm(forms.ModelForm):
    class Meta:
        model = StoredHttpRequest
        fields = ('priority', )
