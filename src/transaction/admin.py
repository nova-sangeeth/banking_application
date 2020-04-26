from django.contrib import admin

# Register your models here.
from .models import Transaction_model

admin.site.register(Transaction_model)
