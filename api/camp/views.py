from typing import Optional, List
import datetime

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from . import models, serializers


def _parse_date(
        date_time: Optional[str]) -> (
            Optional[datetime.date]):
    if not date_time:
        return None

    try:
        return datetime.datetime.strptime(
            date_time, format="%Y-%m-%d"
        ).date()
    except ValueError:
        return None


class CampEventView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CampEventSerializer

    def get(self, request: Request):
        qparams = request.query_params

        camping_type = qparams.get("type")
        if camping_type == "militaryPatriotic":
            camping_type = "army"

        date_begin = _parse_date(qparams.get("start"))

        date_end = _parse_date(qparams.get("end"))

        season = qparams.get("time")
        if season == "autumn":
            season = "fall"

        serializer = self.serializer_class(
            self.filter_camp_events(
                camping_type, date_begin, date_end, season),
            many=True
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    @staticmethod
    def filter_camp_events(
        camping_type: Optional[str],
        date_begin: Optional[datetime.date],
        date_end: Optional[datetime.date],
        season: Optional[str]
    ) -> List[models.CampEventModel]:
        """Фильтрация всех смен по параметрам"""
        return models.CampEventModel.objects.filter(
            **({"camping_type": camping_type}
               if camping_type else {}),

            **({"date_begin__gte": date_begin}
               if date_begin else {}),

            **({"date_end__lte": date_end}
               if date_end else {}),

            **({"season": season}
               if season else {}),
        )
