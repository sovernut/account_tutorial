from django.shortcuts import render
from django.http import HttpResponse
from .models import Account,Transaction

def index(request):
    content = "Testcontent"
    return render(request,"account/index.html",{"contentinHTML":content})
