from django.shortcuts import render
from django.http import HttpResponse
from .models import Account,Transaction

def index(request):
    account = Account.objects.order_by('-account_name')
    return render(request,"account/index.html",{"account":account})
    
def detail(request,account_id):
    account = Account.objects.get(pk=account_id)
    return render(request,"account/detail.html",{"account":account})
