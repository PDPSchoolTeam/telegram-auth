from django.urls import path

from apps.views import TelegramApiView, TelegramUserListAPIView, TelegramUserDetailAPIView

urlpatterns = [
    path('auth/tg', TelegramApiView.as_view(),name="telegram-auth"),
    path('auth/users', TelegramUserListAPIView.as_view(),name="telegram-user-list"),
    path('auth/users/<int:pk>', TelegramUserDetailAPIView.as_view(),name="telegram-user-detail"),
]
