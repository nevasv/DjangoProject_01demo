from django.contrib import admin
from django.urls import path, include
from bot.views import bot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', bot),
]
