from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import serializers

from . import models
from api.account.models import create_role_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = (
            'username', 'email', 'phone',
            'firstname', 'lastname', 'patronymic',
            'role', 'is_staff', 'email_confirmed', 'date_joined'
        )


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken('No valid token found in cookie \'refresh_token\'')


class RegistrationSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    patronymic = serializers.CharField()
    
    class Meta:
        model = models.UserModel
        fields = (
            'username', 'email', 'phone', 'role',
            'firstname', 'lastname', 'patronymic',
            "password"
        )
    
    def create(self, validated_data) -> models.UserModel:
        user = models.UserModel(**validated_data)

        user.set_password(self.validated_data.get("password"))
        user.save()
        
        create_role_model(user, self.initial_data.get("citizenship", "россия").lower())

        return user


class ConfirmCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConfirmCodeModel
        fields = ('code', )
