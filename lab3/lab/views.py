from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from lab.models import Client, Transaction
from django.urls import reverse

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')
    else:
        username = request.user.username
        client = Client.objects.get(name = username)
        balance = client.balance
        context = {'balance': balance}
        return render(request, 'index.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                try:
                    client = Client.objects.get(name = username)
                except Client.DoesNotExist:
                    client = Client(name = username, balance = 0)
                    client.save()
                balance = client.balance
                context = {'balance': balance}
                return render(request,'index.html', context)
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            client = Client(name = username, balance = 0)
            client.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
    else:
        user_form = UserCreationForm(request.POST)
    context = {'user_form':user_form, 'registered':registered}
    return render(request,'registration.html', context)

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def main(request):
        transactions = Transaction.objects.all()
        context = {'transactions': transactions}
        return render(request, 'main.html', context)

@login_required
def makeTransaction(request):
    sender_name = request.user.username
    receiver_name = request.POST['receiver_name']
    sender = Client.objects.get(name=sender_name)
    receiver = Client.objects.get(name=receiver_name)
    transaction = Transaction(sender=sender, sum=int(request.POST['sum']), receiver=receiver)
    transaction.save()
    sender.balance -= request.POST['sum']
    receiver.balance += request.POST['sum']
    return HttpResponseRedirect(reverse('index'))

@login_required
def replenish(request):
    sum = int(request.POST['replenish_sum'])
    user = request.user.username
    client = Client.objects.get(name=user)
    client.balance = client.balance + sum
    client.save()

    return HttpResponseRedirect(reverse('index'))
