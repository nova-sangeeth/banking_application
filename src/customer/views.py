from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404

# Create your views here.
from .forms import customer_details_form
from .models import customer
from django.contrib.auth.models import User, Group


def index(request):
    return HttpResponse('Hello There')


def register(request):
    user = User.objects.get(username=request.user.username)
    Customer = customer(user=user)
    form = customer_details_form(request.POST or None, instance=customer)
    # context = {"customerform": form, "type": "register"}
    if request .method == "POST":
        if form.is_valid():
            f = form.save()
            f.account_no = f.acc_no()
            f.save()
            group = get_object_or_404(Group, name='Customer')
            user.group.add(group)
    return render(request, "registeration.html", {"form": form})


def edit(request):
    user = get_object_or_404(User, username=request.user.username)
    Customer = get_object_or_404(customer, user=user)
    form = customer_details_form(request.POST or None, instance=customer)
    # form = customer_details_form(request.POST or None)
    if request.method == "POST":
        print("success")
        if form.is_valid():
            f = form.save()
            f.account_no = f.acc_no()
            f.save()

    return render(request, "edit.html", {"form": form})


def profile(request):
    user = customer.objects.filter(user=request.user)
    return render(request, "profile.html", {"set": user})


def withdraw(request):
    pass


def amount(request):
    pass


def amount_to(request):
    pass


def transfer(request):
    pass


def result(request):
    pass
