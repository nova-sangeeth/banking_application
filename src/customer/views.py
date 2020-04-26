from django.shortcuts import render, HttpResponse

# Create your views here.
from .forms import customer_details_form
from .models import customer_details


def index(request):
    return HttpResponse('Hello There')
