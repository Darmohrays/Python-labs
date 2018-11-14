from django.test import TestCase
from .models import Client, Transaction
from django.urls import reverse

# Create your tests here.

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name="Test", balance=100)

    def test_client(self):
        client = Client.objects.get(name="Test")
        self.assertEqual(client.name, "Test")
        self.assertEqual(client.balance, 100)

class TransactionTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name="Sender1", balance=1000)
        Client.objects.create(name="Receiver1", balance=2000)
        Transaction.objects.create(sender_name="Sender1",  receiver_name="Receiver1", sum=100)
        Transaction.objects.create(sender_name="Receiver1",  receiver_name="Sender1", sum=200)

    def test_transaction(self):
        transaction = Transaction.objects.get(sender_name="Sender1")
        self.assertEqual(transaction.sender_name, "Sender1")
        self.assertEqual(transaction.receiver_name, "Receiver1")
        self.assertEqual(transaction.sum, 100)

        transaction.makeTransactiob()

class UrlsTestCase(TestCase):
    def test_index(self):
        # Get the client
        response = self.client.get(reverse('index'))
         # Check the status code
        self.assertEqual(response.status_code, 200)
        
    def test_base(self):
         # Get the client
        response = self.client.get(reverse('base'))
         # Check the status code
        self.assertEqual(response.status_code, 302)
    def test_register(self):
         # Get the client
        response = self.client.get(reverse('registration'))
         # Check the status code
        self.assertEqual(response.status_code, 200)

