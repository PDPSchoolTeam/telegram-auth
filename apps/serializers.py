from rest_framework import serializers

from apps.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'telegram_id')

    def validate_telegram_id(self, value):
        """Ensure telegram_id is always required"""
        if not value:
            raise serializers.ValidationError("Telegram ID is required.")
        return value
