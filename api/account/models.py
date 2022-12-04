from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from api.address import models as address_models
from .countries import COUNTRIES


def create_role_model(user, citizenship):
    role: str = user.role
    
    if role != "client":
        return
    
    RepresentativeModel.objects.create(
        user=user,
        firstname=user.firstname,
        lastname=user.lastname,
        patronymic=user.patronymic,
        phone=user.phone,
        citizenship=citizenship
    )


class RussianPassportModel(models.Model):
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
    
    class Meta:
        db_table = "account__russian_passport"
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"
    
    def __str__(self) -> str:
        return f"{self.pk}: {self.series} {self.number} ({self.type})"
    

class ForeignPassportModel(models.Model):
    series = models.TextField(
        "Серия"
    )
    number = models.TextField(
        "Номер"
    )
    date_of_issue = models.DateTimeField(
        "Дата выдачи"
    )
    duration = models.DateTimeField(
        "Срок действия", null=True
    )

    class Meta:
        db_table = "account__foreign_passport"
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"
    
    def __str__(self) -> str:
        return f"{self.pk}: {self.series} {self.number}"
    

class BirthCertificateModel(models.Model):
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
    
    TYPES = (
        ("foreign", "Зарубежное"),
        ("russian", "Российское"),
    )
    
    class Meta:
        db_table = "account__birth_certificate"
        verbose_name = "Свидетельство о рождении"
        verbose_name_plural = "Свидетьства о рождении"
    
    def __str__(self) -> str:
        return f"{self.pk}: {self.series} {self.number}"


class ChildModel(models.Model):
    citizenship = models.CharField(
        "Гражданство", max_length=128,
        choices=COUNTRIES, default="россия"
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

    registration_address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес регистрации",
        related_name="child_registration_address",
        null=True, blank=True
    )
    residence_address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес проживания",
        related_name="child_residence_address",
        null=True, blank=True
    )
    
    DOCUMENT_TYPES = (
        ('passport', 'Паспорт'),
        ('birth_certificate', 'Свидетельство о рождении')
    )
    
    document_type = models.CharField(
        "Тип документа", choices=DOCUMENT_TYPES,
        default="passport", max_length=64
    )

    russian_passport = models.ForeignKey(
        RussianPassportModel, models.PROTECT,
        verbose_name="Российский паспорт",
        null=True, blank=True
    )
    foreign_passport = models.ForeignKey(
        ForeignPassportModel, models.PROTECT,
        verbose_name="Зарубежный паспорт",
        null=True, blank=True
    )
    birth_certificate = models.ForeignKey(
        BirthCertificateModel, models.PROTECT,
        verbose_name="Свидетельство о рождении",
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
    
    def document(self) -> str:
        if self.document_type == "passport":
            if self.citizenship == "Россия":
                return self.russian_passport
            return self.foreign_passport

        if self.document_type == "birth_certificate":
            return self.birth_certificate

        return ""


class RepresentativeModel(models.Model):
    citizenship = models.CharField(
        "Гражданство", max_length=128,
        choices=COUNTRIES, default="россия"
    )

    user = models.ForeignKey(
        get_user_model(), models.CASCADE,
        null=True, blank=True
    )
    phone = models.CharField(
        "Телефон", max_length=10,
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
    
    registration_address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес регистрации",
        related_name="representative_registration_address",
        null=True, blank=True
    )
    residence_address = models.ForeignKey(
        address_models.AddressModel, models.PROTECT,
        verbose_name="Адрес проживания",
        related_name="representative_residence_address",
        null=True, blank=True
    )
    
    russian_passport = models.ForeignKey(
        RussianPassportModel, models.PROTECT,
        verbose_name="Российский паспорт",
        blank=True, null=True
    )
    foreign_passport = models.ForeignKey(
        ForeignPassportModel, models.PROTECT,
        verbose_name="Зарубежный паспорт",
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
    
    def document(self) -> str:
        if self.citizenship == "Россия":
            return self.russian_passport
        
        return self.foreign_passport
