from rest_framework import serializers

from . import models


class CampEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CampEventModel
        fields = "__all__"
        depth = 2

    def save(self, *args, **kwargs):
        """Поправляем тип смены при необходимости"""

        if self.season != "summer":
            self.camping_type = "stationary"

        return super().save(*args, **kwargs)
