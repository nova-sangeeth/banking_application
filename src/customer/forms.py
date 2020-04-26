from django import forms
from django.forms import ModelForm
from .models import customer_details


class customer_details_form(forms.ModelForm):
    model = customer_details
    field = '__all__'
