from rest_framework import serializers

from apps.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'telegram_id', 'role')
