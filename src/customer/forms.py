from django import forms
from django.forms import ModelForm
from .models import customer
from .validators import phone_number_validator


class customer_details_form(forms.ModelForm):
    phone = forms.IntegerField(validators=[
                               phone_number_validator], widget=forms.NumberInput(attrs={'required': "required"}))

    class Meta:
        model = customer
        field = '__all__'
        exclude = ('user',)
