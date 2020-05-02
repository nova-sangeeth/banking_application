from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from decimal import Decimal
from .forms import customer_details_form
from .models import customer
from django.contrib.auth.models import User, Group
from transaction.models import Transaction_model


def index(request):
    return HttpResponse('Hello There')


def register(request):
    user = User.objects.get(username=request.user.username)
    Customer = customer(user=user)
    form = customer_details_form(request.POST or None, instance=Customer)
    # context = {"customerform": form, "type": "register"}
    if request .method == "POST":
        if form.is_valid():
            f = form.save()
            f.account_no = f.acc_no()
            f.save()
            # group = get_object_or_404(Group, name='Customer')
            # user.group.add(group)
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
    user = customer.objects.filter(user=request.user)
    return render(request, "withdraw.html", {"set": user})


def amount(request):
    user = customer.objects.get(user=request.user)
    transaction = Transaction_model(previous_balance=Decimal(user.balance))
    withdraw = request.POST.get('withdraw')
    transaction.amount = Decimal(withdraw)
    amt = user.get_balance(withdraw, 1)
    if amt == -1:
        messages.error(request, "No Balance!")
    else:
        user.balance = amt
    transaction.current_balance = Decimal(user.balance)
    transaction.user = request.user
    transaction.save()
    user.save()


def deposit(request):
    user = customer.objects.get(user=request.user)
    return render(request, 'deposit.html', {"balance": user.balance})


def amount_to(request):
    user = customer.objects.get(user=request.user)
    transaction = Transaction_model(previous_balance=Decimal(user.balance))
    amount = request.POST.get('deposit')
    transaction.amount = Decimal(amount)
    user.balance = user.get_balance(amount, 2)
    transaction.current_balance = Decimal(user.balance)
    transaction.user = request.user
    transaction.save()
    transaction.transaction_id = transaction.get_transaction_id()
    transaction.type = 'Deposit'
    trasaction.save()
    user.save()

    pass


def transfer(request):
    pass


def result(request):
    pass
