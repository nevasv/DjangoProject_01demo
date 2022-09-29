from django.shortcuts import render


def bot_View(request):
    return render(request, 'index.html')


