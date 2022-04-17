from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from .models import *

class TableDataForm(ModelForm):
    name = forms.CharField(label="Name", required=True)
    characteristics = forms.ModelMultipleChoiceField(
                        queryset=Characteristics.objects.all().order_by('name'),
                        label="Characteristics",
                        widget=forms.CheckboxSelectMultiple)
                        
    attendance = forms.CharField(label="Attendance", required=True)
    stadium = forms.CharField(label="Stadium", required=False)
   
    class Meta:
      model = TableData
      exclude = ['created_at','edited_at']
