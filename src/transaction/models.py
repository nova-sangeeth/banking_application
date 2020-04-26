from django.db import models

# Create your models here.
from django.contrib.auth.models import User

import datetime


class Transaction_model(models.Model):
    Withdrawal = 'Withdrawal'
    Deposit = 'Deposit'
    Transfer = 'Account transfer'
    type_choices = (
        (Withdrawal, 'Withdrawal'),
        (Deposit, 'Deposit'),
        (Transfer, 'Account Transfer'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    previous_balance = models.DecimalField(max_digits=20, decimal_places=2)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_time = models.DateTimeField(default=datetime.datetime.now)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_id = models.CharField(max_length=128)
    type = models.CharField(max_length=128, choices=type_choices)

    def __str__(self):
        return self.transaction_id

    def get_transaction_id(self):
        transaction = str(self.user.username) + '_' + str(self.pk)
        return transaction
