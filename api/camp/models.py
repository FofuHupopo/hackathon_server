from typing import Tuple
from django.contrib.auth import get_user_model
import datetime

from django.db import models

from api.address import models as address_models


CAMPING_TYPES = (
    ("stationary", "Стационарный лагерь"),
    ("army", "Палаточный военно-патриотический лагерь"),
    ("tourist", "Палаточный туристический лагерь")
)


class CampOrganizationModel(models.Model):
    ("""Модель сущности организации, """
     """которая проводит лагерные смены""")

    class Meta:
        db_table = "camp__organization"
        verbose_name = "Лагерь"
        verbose_name_plural = "Лагеря"

    # Раздел "Общая информацияcamp_event о лагере":
    
    user = models.ForeignKey(
        get_user_model(), models.CASCADE,
        verbose_name="Пользователь",
        null=True, blank=True
    )

    title = models.CharField(
        "Название", max_length=32,
        null=False, blank=False
    )

    description = models.CharField(
        "Описание", max_length=1024,
        default=""
    )

    camping_type = models.CharField(
        "Тип лагеря", max_length=64,
        choices=CAMPING_TYPES
    )

    # QuerySet лагерных смен
    camp_events: models.query.QuerySet

    def get_camp_events_by_season(
            self, season_eng: str) -> models.query.QuerySet:
        return self.camp_events.filter(
            season=season_eng
        )

    address = models.ForeignKey(
        address_models.AddressModel,
        models.PROTECT,
        verbose_name="Адрес",
        null=True, blank=True
    )

    day_begin = models.TimeField(
        "Начало трудового дня",
        default=datetime.time(0, 0)
    )

    day_end = models.TimeField(
        "Конец трудового дня",
        default=datetime.time(23, 59, 59, 999999)
    )

    @property
    def operating_mode(self) -> Tuple[datetime.time]:
        """Режим работы лагеря"""
        return (self.day_begin, self.day_end)

    phone_number = models.CharField(
        "Номер телефона для справок",
        max_length=12,
        null=True, blank=True
    )

    # Раздел "Инфраструктура лагеря":

    housing_quantity = models.IntegerField(
        "Количество корпусов",
        default=0
    )

    area = models.IntegerField(
        "Площадь территории",
        default=0
    )

    MEAL_TYPES = (
        ("portioned", "Порционное"),
        ("buffet", "Шведский стол")
    )

    meal_type = models.CharField(
        "Тип питания", max_length=24,
        choices=MEAL_TYPES
    )

    having_sports_objects = models.BooleanField(
        "Наличие спортивных объектов",
        default=False
    )

    having_relaxing_objects = models.BooleanField(
        "Наличие досуговых объектов",
        default=False
    )

    def __str__(self) -> str:
        return f"{self.title}"


class CampEventModel(models.Model):
    """Модель сущности лагерной смены"""

    class Meta:
        db_table = "camp__event"
        verbose_name = "Смена"
        verbose_name_plural = "Смены"

    title = models.CharField(
        "Название",
        max_length=64,
        null=False, blank=False
    )

    camp_organization = models.ForeignKey(
        CampOrganizationModel,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name="camp_events",
        verbose_name="Лагерь-организатор"
    )
    
    description = models.TextField(
        "Описание",
        null=True, blank=True
    )

    camping_type = models.CharField(
        "Тип смены",
        max_length=64,
        choices=CAMPING_TYPES
    )

    date_begin = models.DateField(
        "День начала",
        null=False, blank=False
    )

    date_end = models.DateField(
        "День окончания",
        null=False, blank=False
    )

    @property
    def duration(self) -> int:
        """Количество дней смены"""
        return abs((self.date_end - self.date_begin).days)

    SEASONS = (
        ("spring", "Весенние заезды"),
        ("summer", "Летние заезды"),
        ("fall", "Осенние заезды"),
        ("winter", "Зимние заезды")
    )

    season = models.CharField(
        "Лагерный сезон",
        max_length=32,
        choices=SEASONS
    )

    having_rest_certificate = models.BooleanField(
        "Наличие сертификата на отдых",
        default=False
    )
    
    price = models.IntegerField(
        "Цена", default=0
    )
    
    def __str__(self) -> str:
        return f"{self.title}"

