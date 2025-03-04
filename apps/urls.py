from django.urls import path

from apps.views import TelegramApiView

urlpatterns = [
    path('auth/tg', TelegramApiView.as_view(), name='Auth'),
]
