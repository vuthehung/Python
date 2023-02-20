from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reuquest):
    return HttpResponse('<h1>Hey, Welcome</h1>')
