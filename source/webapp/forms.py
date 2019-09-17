from django import forms
from django.forms import widgets

from webapp.models import status_choices


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    text = forms.CharField(max_length=3000, required=True, label='Текст',   widget=widgets.Textarea)
    date = forms.CharField(max_length=3000, required=True, label='Дата', widget=widgets.SelectDateWidget)
    status = forms.ChoiceField(required=True, label='статус', choices=status_choices)
