from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .tables import user_list_table
from django_tables2 import SingleTableView


def employee_profile(request):
    user_name = User.objects.all()
    table = user_list_table
    return render(request, "employee_profile.html", {'user_name': user_name, 'table': table})
