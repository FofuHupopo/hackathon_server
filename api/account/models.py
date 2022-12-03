from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from api.address import models as address_models


def create_role_model(user):
    role: str = user.role
    
    if role != "client":
        return
    
    RepresentativeModel.objects.create(
        user=user,
        firstname=user.firstname,
        lastname=user.lastname,
        patronymic=user.patronymic,
        phone=user.phone
    )


class PassportModel(models.Model):
    series = models.CharField(
        "Серия", max_length=4
    )
    number = models.CharField(
        "Номер", max_length=6
    )
    date_of_issue = models.DateTimeField(
        "Дата выдачи"
    )
    whom_issued = models.TextField(
        "Кем выдан", null=True
    )
    duration = models.DateTimeField(
        "Срок действия", null=True
    )
    
    PASSPORT_TYPES = (
        ("russian", "Российский"),
        ("foreign", "Зарубежный"),
    )
    
    type = models.CharField(
        "Тип", max_length=16,
        choices=PASSPORT_TYPES, default="russian"
    )
    
    class Meta:
        db_table = "account__passport"
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"
    
    def __str__(self) -> str:
        return f"{self.pk}: {self.series} {self.number} ({self.type})"
    
    def save(self, *args, **kwargs) -> None:
        if self.type == "foreign":
            self.whom_issued = ""
    
        return super().save(*args, **kwargs)


class ChildModel(models.Model):
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
    registration_address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес регистрации", related_name="registration_address",
        null=True, blank=True
    )
    residence_address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес проживания", related_name="residence_address",
        null=True, blank=True
    )
    
    snils = models.CharField(
        "СНИЛС", max_length=11,
        null=True, blank=True
    )
    phone = models.CharField(
        "Телефон", max_length=10,
        null=True, blank=True
    )

    birthday_date = models.DateField(
        "Дата регистрации"
    )
    
    class Meta:
        db_table = "account__child"
        verbose_name = "Ребенок"
        verbose_name_plural = "Дети"
        
    def __str__(self) -> str:
        return f"{self.pk}: {self.firstname} {self.lastname}"


class RepresentativeModel(models.Model):
    user = models.ForeignKey(
        get_user_model(), models.CASCADE,
        null=True, blank=True
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
    phone = models.CharField(
        "Телефон", max_length=10,
        null=True, blank=True
    )
    
    passport = models.ForeignKey(
        PassportModel, models.PROTECT,
        verbose_name="Паспорт",
        blank=True, null=True
    )
    children = models.ManyToManyField(
        ChildModel, verbose_name="Дети",
        blank=True
    )
    
    REPRESENTATIVE_STATUSES = (
        ('parent', 'Родитель'),
        ('representative', 'Законный представитель')
    )
    
    STATUS = models.CharField(
        "Статус", max_length=32,
        choices=REPRESENTATIVE_STATUSES, default="parent"
    )
    
    objects = models.Manager()
    
    class Meta:
        db_table = "account__representative"
        verbose_name = "Представитель"
        verbose_name_plural = "Представители"
        
    def __str__(self) -> str:
        return f"{self.pk}: {self.firstname} {self.lastname}"
