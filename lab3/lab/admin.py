from django.contrib import admin
from .models import Transaction, Client

# Register your models here.

admin.site.register(Client)
admin.site.register(Transaction)