from rest_framework import serializers

from . import models


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PassportModel
        fields = "__all__"

        
class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChildModel
        fields = "__all__"
        depth = 3


class RepresentativeSerializer(serializers.ModelSerializer):
    passport = PassportSerializer()
    children = ChildSerializer(many=True)

    class Meta:
        model = models.RepresentativeModel
        fields = (
            'user', 'phone', 'passport',
            'firstname', 'lastname', 'patronymic',
            'children'
        )
        depth = 4
        
    def update(self, instance: models.RepresentativeModel, validated_data):
        passport = validated_data.get("passport", None)
        
        if passport:
            return self._update_passport(instance, passport)

        return instance
    
    @staticmethod
    def _update_passport(instance: models.RepresentativeModel, passport):
        if instance.passport:
            instance.passport.series = passport.get("series", instance.passport.series)
            instance.passport.number = passport.get("number", instance.passport.number)
            instance.passport.date_of_issue = passport.get("date_of_issue", instance.passport.date_of_issue)
            instance.passport.whom_issued = passport.get("whom_issued", instance.passport.whom_issued)
            instance.passport.duration = passport.get("duration", instance.passport.duration)
            instance.passport.type = passport.get("type", instance.passport.type)

            instance.passport.save()
        else:
            passport = models.PassportModel.objects.create(
                **passport
            )

            instance.passport=passport
            instance.save()

        return instance


class RepresentativePassportSerializer(serializers.ModelSerializer):
    passport = PassportSerializer()

    class Meta:
        model = models.RepresentativeModel
        fields = (
            'passport'
        )
