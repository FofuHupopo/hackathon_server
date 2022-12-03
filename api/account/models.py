from django.db import models
from django.utils import timezone

from api.address import models as address_models


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

    birthday_date = models.DateTimeField(
        "Дата регистрации", default=timezone.now
    )
    
    class Meta:
        db_table = "account__child"
        verbose_name = "Ребенок"
        verbose_name_plural = "Дети"
    


class RepresentativeModel(models.Model):
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
    
    address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес",
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
    
    class Meta:
        db_table = "account__representative"
        verbose_name = "Представитель"
        verbose_name_plural = "Представители"
        
    def __str__(self) -> str:
        return f"{self.pk}: {self.firstname} {self.lastname}"
