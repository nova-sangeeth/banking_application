from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def employee_profile(request):
    user_name = User.objects.all()
    return render(request, "employee_profile.html", {'user_name': user_name})
