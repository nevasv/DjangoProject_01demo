from django.shortcuts import render
from django.http import HttpResponse


def botView(request):
    return HttpResponse('Я бот telegram, принимаю webhooks')

# Create your views here.
