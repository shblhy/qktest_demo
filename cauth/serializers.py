from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'email', 'telephone', 'status', 'is_staff', "is_superuser", 'last_login', 'groups')


class UserEasySerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('id', 'username', 'nickname')
