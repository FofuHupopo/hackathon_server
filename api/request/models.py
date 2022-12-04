from django.db import models

from api.account.models import RepresentativeModel, ChildModel
from api.camp.models import CampEventModel


class RequestModel(models.Model):
    representative = models.ForeignKey(
        RepresentativeModel, models.CASCADE,
        verbose_name="Представитель",
    )
    child = models.ForeignKey(
        ChildModel, models.CASCADE,
        verbose_name="Ребенок",
    )
    camp_event = models.ForeignKey(
        CampEventModel, models.CASCADE,
        verbose_name="Лагерная смена"
    )
    
    class Meta:
        db_table = "request__request"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        
    def __str__(self) -> str:
        return f"{self.pk}: {self.representative}, {self.child}, {self.camp_event}"
