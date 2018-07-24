from django.contrib.auth import authenticate
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


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField(label='用户名')
    password = serializers.CharField(label='密码')
    default_error_messages = {
        'invalid_login': "请输入正确的用户名和密码，注意大小写",
        'inactive': "该账号已被禁用.",
    }
    def __init__(self, instance=None, data={}, **kwargs):
        self.instance = None
        self.initial_data = data
        self.request = kwargs.pop('request', None)
        self.partial = kwargs.pop('partial', False)
        self._context = kwargs.pop('context', {})
        kwargs.pop('many', None)
        super(serializers.Serializer, self).__init__(**kwargs)

    @property
    def user(self):
        if hasattr(self, 'user_cache'):
            return self.user_cache

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                self.fail('invalid_login')
            else:
                if not self.user_cache.is_active:
                    self.fail('inactive')
        return attrs
