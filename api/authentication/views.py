from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings

from api.email import SendMailManager
from . import serializers
from . import models


class RegistrationView(APIView):
    serializer_class = serializers.RegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        
        serializer = serializers.UserSerializer(
            user
        )
        
        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
        
        
class UserLogoutView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request: Request) -> Response:
        response = Response(status=status.HTTP_200_OK)

        if response.cookies.get("refresh_token"):
            response.data = {"detail": "Пользователь вышел из аккаунта"}
        else:
            response.data = {"detail": "Вы не были аутентифицированы"}

        response.delete_cookie("refresh_token")

        return response


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
            # del response.data['refresh']

        if response.data.get("access"):
            access = AccessToken(response.data["access"])
            user = get_user_model().objects.filter(id=access["user_id"]).first()

            if user:
                serialized_user = serializers.UserSerializer(user)

                response.data["user"] = serialized_user.data

        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = serializers.CookieTokenRefreshSerializer
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
            # del response.data["refresh"]

        if response.data.get("access"):
            access = AccessToken(response.data["access"])
            user = get_user_model().objects.filter(id=access["user_id"]).first()

            if user:
                serialized_user = serializers.UserSerializer(user)

                response.data["user"] = serialized_user.data

            print(access)

        return super().finalize_response(request, response, *args, **kwargs)

    

class SendCodeView(APIView):
    serializer_class = serializers.ConfirmCodeSerializer
    
    def get(self, request: Request) -> Response:
        if request.user.email_confirmed:
            return Response(
                {
                    "detail": "Ваша почта уже подтверждена"
                },
                status.HTTP_400_BAD_REQUEST
            )
        
        code = models.ConfirmCodeModel.generate_code(
            request.user
        )
            
        SendMailManager(request.user.email).send(
            "Подтверждение почты",
            f"Код подверждения почты: {code.code}"
        )
        
        return Response(
            {
                "detail": "Код отправлен на почту"
            },
            status.HTTP_200_OK
        )


class ConfirmCodeView(APIView):
    serializer_class = serializers.ConfirmCodeSerializer

    def post(self, request: Request) -> Response:
        code = request.data.get("code", None)

        if not code:
            return Response(
                {
                    "detail": "Код не был передан"
                },
                status.HTTP_400_BAD_REQUEST
            )

        code: models.ConfirmCodeModel = get_object_or_404(
            models.ConfirmCodeModel,
            code=code
        )

        if code.is_valid():
            user = code.user
            code.confirm_user()

            serializer = serializers.UserSerializer(
                user
            )

            return Response(
                serializer.data,
                status.HTTP_200_OK
            )

        return Response(
            {
                "detail": "Код устарел"
            },
            status.HTTP_400_BAD_REQUEST
        )
