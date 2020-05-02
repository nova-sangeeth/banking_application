from django import forms
from django.forms import ModelForm
from .models import customer


class customer_details_form(forms.ModelForm):
    class Meta:
        model = customer
        widgets = {
            "name": forms.TextInput(attrs={'required': "required"}),
            "age": forms.NumberInput(attrs={'required': "required"}),
            "street": forms.TextInput(attrs={'required': "required"}),
            "city": forms.TextInput(attrs={'required': "required"}),
            "phone": forms.TextInput(attrs={'required': "required"}),
            "state": forms.TextInput(attrs={'required': "required"}),
            "country": forms.TextInput(attrs={'required': "required"}),
            "pincode": forms.NumberInput(attrs={'required': "required"}),
            "balance": forms.NumberInput(attrs={'required': "required"}),
        }
        fields = ['name', 'age', 'phone', 'street', 'city',
                  'state', 'country', 'pincode', 'balance']
