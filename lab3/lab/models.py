from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length = 50)
    balance = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    sender = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="sender")
    sum = models.IntegerField(default=0)
    receiver = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="receiver")
    transaction_date = models.DateTimeField(auto_now_add=True, blank=True)