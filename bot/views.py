from project01.shortcuts import render
from project01.http import HttpResponse


def botView(request):
    return HttpResponse('Я бот telegram, принимаю webhooks')

# Create your views here.
