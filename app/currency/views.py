from django.shortcuts import render
from django.http import HttpResponse

def hello(reqiuests):
    return HttpResponse("Hello World!")
