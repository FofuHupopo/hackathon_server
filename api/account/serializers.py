from rest_framework import serializers

from api.authentication.serializers import UserSerializer
from . import models


class RussianPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RussianPassportModel
        fields = "__all__"
        

class ForeignPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForeignPassportModel
        fields = "__all__"

        
class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChildModel
        fields = "__all__"
        depth = 3


class RepresentativeSerializer(serializers.ModelSerializer):
    russian_passport = RussianPassportSerializer()
    foreign_passport = ForeignPassportSerializer()
    children = ChildSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = models.RepresentativeModel
        fields = (
            'user', 'phone', 'russian_passport', 'foreign_passport',
            'firstname', 'lastname', 'patronymic', 'citizenship',
            'children'
        )
        depth = 4
        
    def update(self, instance: models.RepresentativeModel):
        passport = self.initial_data.get("passport", None)
        print(passport)
        
        if passport:
            return self._update_passport(instance, passport)

        return instance
    
    @staticmethod
    def _update_passport(instance: models.RepresentativeModel, passport):
        if instance.citizenship == "россия":
            if instance.russian_passport:
                instance.russian_passport.series = passport.get("series", instance.russian_passport.series)
                instance.russian_passport.number = passport.get("number", instance.russian_passport.number)
                instance.russian_passport.date_of_issue = passport.get("date_of_issue", instance.russian_passport.date_of_issue)
                instance.russian_passport.whom_issued = passport.get("whom_issued", instance.russian_passport.whom_issued)

                instance.russian_passport.save()
            else:
                passport_serializer = RussianPassportSerializer(
                    data=passport
                )
                passport_serializer.is_valid(raise_exception=True)
                passport = passport_serializer.save()

                instance.russian_passport = passport
                instance.save()
        else:
            if instance.foreign_passport:
                instance.foreign_passport.series = passport.get("series", instance.foreign_passport.series)
                instance.foreign_passport.number = passport.get("number", instance.foreign_passport.number)
                instance.foreign_passport.date_of_issue = passport.get("date_of_issue", instance.foreign_passport.date_of_issue)
                instance.foreign_passport.duration = passport.get("duration", instance.foreign_passport.duration)

                instance.foreign_passport.save()
            else:
                passport_serializer = ForeignPassportSerializer(
                    data=passport
                )
                passport_serializer.is_valid(raise_exception=True)
                passport = passport_serializer.save()

                instance.foreign_passport = passport
                instance.save()

        return instance
