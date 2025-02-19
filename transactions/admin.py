from django.contrib import admin

# from transactions.models import Transaction
from .models import Transaction
admin.site.register(Transaction)
