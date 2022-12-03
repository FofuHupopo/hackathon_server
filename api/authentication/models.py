from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import random

from .manager import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Логин', max_length=64, unique=True,
    )
    email = models.EmailField(
        'Почта', unique=True,
    )
    phone = models.CharField(
        'Телефон', max_length=10, unique=True
    )

    firstname = models.CharField(
        'Имя', max_length=64, blank=True,
    )
    lastname = models.CharField(
        'Фамилия', max_length=64, blank=True,
    )
    patronymic = models.CharField(
        'Отчество', max_length=64,
        null=True, blank=True
    )

    ROLE_CHOICES = (
        ("client", "Клиент"),
        ("organization", "Организация"),
        ("staff", "Сотрудник"),
    )

    role = models.CharField(
        'Роль', max_length=12,
        choices=ROLE_CHOICES, default="client"
    )

    is_staff = models.BooleanField(
        "Сотрудник?", default=False
    )
    is_active = models.BooleanField(
        "Активный?", default=True,
        help_text="Включено, когда аккаунт не в бане"
    )
    is_superuser = models.BooleanField(
        "Администратор", default=False
    )
    email_confirmed = models.BooleanField(
        "Почта подверждена?", default=False
    )

    date_joined = models.DateTimeField(
        "Дата регистрации", default=timezone.now
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email', 'phone'
    ]

    objects = UserManager()

    class Meta:
        db_table = 'auth__user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f"{self.pk}: {self.username}, {self.email}, {self.phone}"

    @classmethod
    def it_exists(cls, email: str) -> bool:
        return bool(cls.objects.filter(email=email))


def code_lifetime():
    return timezone.now() + timezone.timedelta(minutes=5)


def generate_code():
    return str(random.randint(111111, 999999))


class ConfirmCodeModel(models.Model):
    code = models.CharField(
        "Код", max_length=6
    )
    lifetime = models.DateTimeField(
        "Жив до", default=code_lifetime
    )
    user: UserModel = models.ForeignKey(
        UserModel, models.CASCADE,
        verbose_name="Для пользователя"
    )

    class Meta:
        db_table = "auth__confirm_code"
        verbose_name = "Код"
        verbose_name_plural = "Коды"

    def __str__(self) -> str:
        return f"{self.pk}: {self.code} - {self.user.username}"

    def is_valid(self) -> bool:
        return timezone.now() <= self.lifetime

    def confirm_user(self) -> None:
        self.user.email_confirmed = True
        self.user.save()

        self.delete()

    @classmethod
    def generate_code(cls, user):
        return cls.objects.create(
            code=generate_code(),
            user=user
        )