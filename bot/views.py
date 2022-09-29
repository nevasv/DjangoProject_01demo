from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def bot(request):
    return render(request, 'bot/bot.html')



