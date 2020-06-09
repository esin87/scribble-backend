from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'name')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
