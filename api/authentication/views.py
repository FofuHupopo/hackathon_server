from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings

from . import serializer
from . import models


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                value=response.data["refresh"],
                max_age=settings.SIMPLE_JWT["MAX_AGE"],
                # expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            )
            del response.data['refresh']

        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

    def finalize_response(self, request, response: Response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                value=response.data["refresh"],
                max_age=settings.SIMPLE_JWT["MAX_AGE"],
                # expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                domain=settings.SIMPLE_JWT['AUTH_COOKIE_DOMAIN']
            )

            del response.data["refresh"]

        return super().finalize_response(request, response, *args, **kwargs)