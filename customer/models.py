from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


state_choice = (
    ("none", "none"),
    ("Assam", "Assam"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Karnataka", "Karnataka"),
    ("Goa", "Goa"),
    ("Rajasthan", "Rajasthan"),
    ("Bihar", "Bihar"),
)

country_choice = (("None", "None"), ("India", "India"))


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    age = models.PositiveIntegerField()
    phone = models.CharField(null=True, max_length=15)

    street = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=128, choices=state_choice, null=True)
    country = models.CharField(max_length=128, choices=country_choice, null=True)
    pincode = models.IntegerField(null=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Balance"
    )
    account_number = models.CharField(
        max_length=128, editable=False, default=uuid.uuid4
    )

    def __str__(self):
        return str(self.user)

    def acc_no(self):
        acc_no = "BANKACC" + str(self.pk)
        return acc_no

    # code to show the balence in the customer's account in the correct format.

    def get_balance(self, amount, code):
        amount = Decimal(amount)
        balance = Decimal(self.balance)
        if code == 1:
            if balance > amount:
                balance = balance - amount
                return balance
            else:
                return -1
        else:
            balance = balance + amount
            return balance
