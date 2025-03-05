from django.urls import path

from apps.views import TelegramApiView, TelegramUserListAPIView

urlpatterns = [
    path('auth/tg', TelegramApiView.as_view()),
    path('auth/users', TelegramUserListAPIView.as_view()),
]
