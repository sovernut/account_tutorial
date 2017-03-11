from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account,Transaction
from django.urls import reverse

def index(request):
    account = Account.objects.order_by('-account_name')
    return render(request,"account/index.html",{"account":account})
    
def detail(request,account_id):
    account = get_object_or_404(Account,pk=account_id)
    return render(request,"account/detail.html",{"account":account})

def add_account(request):
    try:
        get_name = request.POST['account_name']
    except:
        error_msg = "Error !"
    else:
        if get_name.isalpha():
            a = Account(account_name=get_name,total=0)
            a.save()
    return HttpResponseRedirect(reverse('index'))