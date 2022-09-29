from django.contrib import admin
from django.urls import path, include  # новое добавление
from bot.views import bot_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vbot_View),
]
