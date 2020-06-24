from django import forms
from django.forms import ModelForm
from .models import customer


class customer_details_form(forms.ModelForm):
    class Meta:
        model = customer

        fields = [
            "name",
            "age",
            "phone",
            "street",
            "city",
            "state",
            "country",
            "pincode",
            "balance",
        ]
        exclude = ("user",)

