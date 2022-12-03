from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        'Логин', max_length=64, unique=True,
    )
    email = models.EmailField(
        'Почта', unique=True,
    )
    phone = models.CharField(
        'Телефон', max_length=14, unique=True
    )

    firstname = models.CharField(
        'Имя', max_length=64, blank=True,
    )
    lastname = models.CharField(
        'Фамилия', max_length=64, blank=True,
    )

    ROLE_CHOICES = (
        ("teacher", "Учитель"),
        ("parent", "Родитель"),
        ("student", "Ученик")
    )

    role = models.CharField(
        'Роль', max_length=12,
        choices=ROLE_CHOICES, default="student"
    )

    is_online = models.BooleanField(
        'Онлайн?', default=False
    )
    is_staff = models.BooleanField(
        "Модератор?", default=False
    )
    is_active = models.BooleanField(
        "Активный?", default=True,
        help_text="Включено, когда аккаунт не в бане"
    )
    is_superuser = models.BooleanField(
        "Администратор", default=False
    )

    date_joined = models.DateTimeField(
        "Дата регистрации", default=timezone.now
    )
    last_visit = models.DateTimeField(
        "Последнее посещение", default=timezone.now
    )

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = [
        'email', 'phone'
    ]

    objects = UserManager()

    class Meta:
        db_table = 'auth__user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f"{self.pk}: {self.login}, {self.email}"

    @classmethod
    def it_exists(cls, email: str) -> bool:
        return bool(cls.objects.filter(email=email))
