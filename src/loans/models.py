from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class customer_loans_model(models.Model):
    loan_choices = (
        (auto: "auto_loans"),
        (personal: "personal_loans"),
        (home: "home_loans"),
        (student: "student_loans"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    previous_balance = models.DecimalField(max_digits=20, decimal_places=2)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_time = models.DateTimeField(default=datetime.datetime.now)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_id = models.CharField(max_length=128)
    loan_id = models.CharField(max_length=128)
    type = models.CharField(max_length=128, choices=loan_choices)

    def __str__(self):
        return self.transaction_id

    def get_loan_id(self):
        loan = str(self.user.username) + '_' + str(self.pk)
        return loan
