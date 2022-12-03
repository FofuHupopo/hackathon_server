from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        user_email = kwargs.get('username')
        password = kwargs.get('password')

        if not user_email:
            return None

        try:
            user = get_user_model().objects.get(email=user_email)

            if user.check_password(password) is True:
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        user_model = get_user_model()

        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None


class PhoneBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        user_phone = kwargs.get('username')
        password = kwargs.get('password')

        if not user_phone:
            return None

        try:
            user = get_user_model().objects.get(phone=user_phone)

            if user.check_password(password) is True:
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        user_model = get_user_model()

        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
