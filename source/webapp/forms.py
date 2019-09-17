from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class PlanForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status')
    text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)
    done_at = forms.DateField(widget=widgets.SelectDateWidget, required=True)