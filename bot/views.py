from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def bot_View(request):
    return render(request, 'bot/index.html')



