from django.shortcuts import (
    render,
    HttpResponse,
    get_list_or_404,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.models import User

# Create your views here.
from .tables import user_list_table
from django_tables2 import SingleTableView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from customer.models import customer


def employee_profile(request):
    user_name = User.objects.all()
    table = user_list_table
    return render(
        request, "employee_profile.html", {"user_name": user_name, "table": table}
    )


def customer(request):
    cutomers = customer.objects.all()
    paginator = Paginator = (customers, 10)
    page = request.GET.get("page")
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, "profile.html", {"customers": customers})

