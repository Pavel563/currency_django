# from django.shortcuts import render
from django.http import HttpResponse
from currency.utils import generate_password as gp


def hello(reqiuests):
    return HttpResponse("Hello World!")


def generate_password(reqiuests):
    password = gp()
    return HttpResponse(password)
