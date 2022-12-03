from django.db import models


class RegionModel(models.Model):
    country = models.CharField(
        "Страна", max_length=128,
        default="Россия",
    )
    region = models.CharField(
        "Регион", max_length=128,
        null=True,
    )
    
    class Meta:
        db_table = "address__region"
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class CityModel(models.Model):
    region = models.ForeignKey(
        RegionModel, models.CASCADE,
        verbose_name="Регион", 
    )
    area = models.CharField(
        "Район", max_length=128,
    )
    city = models.CharField(
        "Город", max_length=128,
    )

    objects = models.Manager()

    class Meta:
        db_table = "address__city"
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self) -> str:
        return f"{self.pk}: {self.region}, {self.city}"



class AddressModel(models.Model):
    city = models.ForeignKey(
        CityModel, models.CASCADE, verbose_name="Город",
    )
    street = models.TextField(
        "Улица"
    )
    number = models.TextField(
        "Номер дома"
    )
    corpus = models.TextField(
        "Корпус",
        null=True, blank=True
    )
    flat_number = models.TextField(
        "Номер квартиры"
    )
    
    objects = models.Manager()

    class Meta:
        db_table = "address__address"
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self) -> str:
        return f"{self.pk}: {self.street} {self.number} {self.flat_number}"
