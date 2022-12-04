from rest_framework import serializers

from . import models


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestModel
        fields = "__all__"
        depth = 5
