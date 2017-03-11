from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account,Transaction
from django.urls import reverse
from django.utils import timezone # for adding transaction

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
        error_msg = "Error! account name."
    else:
        if get_name.isalpha():
            a = Account(account_name=get_name,total=0)
            a.save()
    return HttpResponseRedirect(reverse('index'))
    
def del_account(request):
    error_msg = ""
    try:
        get_id = request.POST['account_id']
    except:
        error_msg = "Error! account delete."
    else:
        a = Account.objects.get(id=get_id)
        a.delete()
    return HttpResponseRedirect(reverse('index'))
    
def editname(request,account_id):
    account = get_object_or_404(Account, pk=account_id)
    try:
        get_name = request.POST['name']
    except:
        error = 1
    else:
        account.account_name = get_name
        account.save()
    return HttpResponseRedirect(reverse('detail', args=(account_id,)))
    
def add_transaction(request,account_id):
    account = get_object_or_404(Account, pk=account_id)
    try:
        get_detail = request.POST['detail']
        get_value = int(request.POST['value'])
        get_ttype = request.POST['t_type']
    except:
        pass
    else:
        if get_ttype == 'expense':
            get_value = -1*get_value
        account.total = account.total + get_value
        account.save()
        account.transaction_set.create(detail=get_detail,value=get_value,date=timezone.now())
    return HttpResponseRedirect(reverse('detail', args=(account_id,)))