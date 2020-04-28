from django.shortcuts import render, HttpResponse

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
    return render(request, "index.html", {"form": form})


def edit(request):
    pass


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
