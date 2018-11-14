from .models import Client, Transaction
from django.test import TestCase
from django.urls import reverse
from . import views 
import pytest
from django.contrib.auth.forms import UserCreationForm

@pytest.mark.django_db
class ClientTest(TestCase):
    def test_song(self):
        client = Client(name="Test", balance=100)
        client.save()
        assert client.name=="Test"
        assert client.balance==100
        assert client.__str__()=="Test"

    
@pytest.mark.django_db
class TransactionTest(TestCase):
    def test_transaction(self):
        client = Client(name="TestSender", balance=125)
        client.save()

        client = Client(name="TestReceiver", balance=95)
        client.save()

        transaction = Transaction(sender_name="TestSender", receiver_name="TestReceiver",sum=100)
        transaction.save()
        assert transaction.sender_name=="TestSender"
        assert transaction.receiver_name=="TestReceiver"
        assert transaction.sum==100
        assert transaction.makeTransaction() == None

class TestUrls(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200

    def test_registration(self):
        response = self.client.get(reverse('registration'))
        assert response.status_code == 200

    def test_main(self):
        response = self.client.get(reverse('main'))
        assert response.status_code == 302

@pytest.mark.django_db
class TestViews(TestCase):
    def test_login(self):
        client = Client(name="username", balance=100)
        client.save()
        data = {"username": "test", "password1": "testpassword",  "password2": "testpassword"}
        user_form = UserCreationForm(data)
        user_form.save()
        response = self.client.post(reverse("user_login"), {"username": "test", "password": "testpassword"})
        assert response.status_code == 200

    def test_registration(self):
        data = {"username": "test", "password1": "testpassword",  "password2": "testpassword"}
        response = self.client.post(reverse("registration"), data)
        assert response.status_code == 302