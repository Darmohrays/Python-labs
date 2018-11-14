from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length = 50)
    balance = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    sender_name = models.CharField(max_length = 50)
    sum = models.IntegerField(default=0)
    receiver_name = models.CharField(max_length = 50)
    transaction_date = models.DateTimeField(auto_now_add=True, blank=True)
    def makeTransaction(self):
        sender = Client.objects.get(name = self.sender_name)
        sender.balance = int(sender.balance) - int(self.sum)
        receiver = Client.objects.get(name = self.receiver_name)
        receiver.balance = int(receiver.balance) + int(self.sum)
        sender.save()
        receiver.save()