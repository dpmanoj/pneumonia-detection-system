from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    return render(requests,'ums/index.html')